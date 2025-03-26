import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def load_results(results_dir):
    """Load all results from the results directory"""
    results = {}
    
    for benchmark in ["mind2web", "webarena", "webvoyager", "webcanvas"]:
        results_file = os.path.join(results_dir, f"{benchmark}_results.json")
        if os.path.exists(results_file):
            with open(results_file, 'r') as f:
                results[benchmark] = json.load(f)
    
    return results

def analyze_success_rates(results):
    """Analyze success rates across benchmarks"""
    success_rates = {}
    
    for benchmark, benchmark_results in results.items():
        success_count = sum(1 for r in benchmark_results if r.get("success", False))
        total_count = len(benchmark_results)
        success_rate = success_count / total_count if total_count > 0 else 0
        success_rates[benchmark] = success_rate * 100
    
    return success_rates

def analyze_time_taken(results):
    """Analyze time taken per task across benchmarks"""
    time_stats = {}
    
    for benchmark, benchmark_results in results.items():
        times = [r.get("time_taken", 0) for r in benchmark_results]
        time_stats[benchmark] = {
            "mean": sum(times) / len(times) if times else 0,
            "median": sorted(times)[len(times)//2] if times else 0,
            "min": min(times) if times else 0,
            "max": max(times) if times else 0
        }
    
    return time_stats

def analyze_token_usage(results):
    """Analyze token usage across benchmarks"""
    token_stats = {}
    
    for benchmark, benchmark_results in results.items():
        total_tokens = [r.get("token_usage", {}).get("total", 0) for r in benchmark_results]
        token_stats[benchmark] = {
            "mean": sum(total_tokens) / len(total_tokens) if total_tokens else 0,
            "median": sorted(total_tokens)[len(total_tokens)//2] if total_tokens else 0,
            "min": min(total_tokens) if total_tokens else 0,
            "max": max(total_tokens) if total_tokens else 0,
            "total": sum(total_tokens)
        }
    
    return token_stats

def analyze_steps(results):
    """Analyze steps taken per task across benchmarks"""
    step_stats = {}
    
    for benchmark, benchmark_results in results.items():
        steps = [len(r.get("steps", [])) for r in benchmark_results]
        step_stats[benchmark] = {
            "mean": sum(steps) / len(steps) if steps else 0,
            "median": sorted(steps)[len(steps)//2] if steps else 0,
            "min": min(steps) if steps else 0,
            "max": max(steps) if steps else 0
        }
    
    return step_stats

def generate_plots(results, output_dir):
    """Generate plots for visualization"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Check if results are empty
    if not results:
        print("No results to analyze. Creating placeholder report.")
        with open(os.path.join(output_dir, "evaluation_report.md"), "w") as f:
            f.write("# Browser Use Evaluation Report\n\n")
            f.write("No evaluation results available yet. Please run the evaluations first.\n")
        return
    
    # Success rate plot
    success_rates = analyze_success_rates(results)
    if success_rates:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(success_rates.keys()), y=list(success_rates.values()))
        plt.title("Success Rate by Benchmark")
        plt.xlabel("Benchmark")
        plt.ylabel("Success Rate (%)")
        plt.savefig(os.path.join(output_dir, "success_rates.png"))
    
    # Time taken plot
    time_stats = analyze_time_taken(results)
    if time_stats:
        plt.figure(figsize=(10, 6))
        data = []
        for benchmark, stats in time_stats.items():
            data.append({"benchmark": benchmark, "time": stats["mean"], "metric": "mean"})
            data.append({"benchmark": benchmark, "time": stats["median"], "metric": "median"})
        
        if data:
            df = pd.DataFrame(data)
            sns.barplot(x="benchmark", y="time", hue="metric", data=df)
            plt.title("Time Taken by Benchmark")
            plt.xlabel("Benchmark")
            plt.ylabel("Time (seconds)")
            plt.savefig(os.path.join(output_dir, "time_taken.png"))
    
    # Token usage plot
    token_stats = analyze_token_usage(results)
    if token_stats:
        plt.figure(figsize=(10, 6))
        data = []
        for benchmark, stats in token_stats.items():
            data.append({"benchmark": benchmark, "tokens": stats["mean"], "metric": "mean"})
            data.append({"benchmark": benchmark, "tokens": stats["median"], "metric": "median"})
        
        if data:
            df = pd.DataFrame(data)
            sns.barplot(x="benchmark", y="tokens", hue="metric", data=df)
            plt.title("Token Usage by Benchmark")
            plt.xlabel("Benchmark")
            plt.ylabel("Tokens")
            plt.savefig(os.path.join(output_dir, "token_usage.png"))
    
    # Steps taken plot
    step_stats = analyze_steps(results)
    if step_stats:
        plt.figure(figsize=(10, 6))
        data = []
        for benchmark, stats in step_stats.items():
            data.append({"benchmark": benchmark, "steps": stats["mean"], "metric": "mean"})
            data.append({"benchmark": benchmark, "steps": stats["median"], "metric": "median"})
        
        if data:
            df = pd.DataFrame(data)
            sns.barplot(x="benchmark", y="steps", hue="metric", data=df)
            plt.title("Steps Taken by Benchmark")
            plt.xlabel("Benchmark")
            plt.ylabel("Steps")
            plt.savefig(os.path.join(output_dir, "steps_taken.png"))
            
def generate_report(results, output_dir):
    """Generate a comprehensive report"""
    success_rates = analyze_success_rates(results)
    time_stats = analyze_time_taken(results)
    token_stats = analyze_token_usage(results)
    step_stats = analyze_steps(results)
    
    report = "# Browser Use Evaluation Report\n\n"
    
    # Success rates
    report += "## Success Rates\n\n"
    report += "| Benchmark | Success Rate |\n"
    report += "|-----------|-------------|\n"
    for benchmark, rate in success_rates.items():
        report += f"| {benchmark} | {rate:.2f}% |\n"
    report += "\n"
    
    # Time taken
    report += "## Time Taken (seconds)\n\n"
    report += "| Benchmark | Mean | Median | Min | Max |\n"
    report += "|-----------|------|--------|-----|-----|\n"
    for benchmark, stats in time_stats.items():
        report += f"| {benchmark} | {stats['mean']:.2f} | {stats['median']:.2f} | {stats['min']:.2f} | {stats['max']:.2f} |\n"
    report += "\n"
    
    # Token usage
    report += "## Token Usage\n\n"
    report += "| Benchmark | Mean | Median | Min | Max | Total |\n"
    report += "|-----------|------|--------|-----|-----|-------|\n"
    for benchmark, stats in token_stats.items():
        report += f"| {benchmark} | {stats['mean']:.2f} | {stats['median']:.2f} | {stats['min']} | {stats['max']} | {stats['total']} |\n"
    report += "\n"
    
    # Steps taken
    report += "## Steps Taken\n\n"
    report += "| Benchmark | Mean | Median | Min | Max |\n"
    report += "|-----------|------|--------|-----|-----|\n"
    for benchmark, stats in step_stats.items():
        report += f"| {benchmark} | {stats['mean']:.2f} | {stats['median']:.2f} | {stats['min']} | {stats['max']} |\n"
    
    # Write report to file
    with open(os.path.join(output_dir, "evaluation_report.md"), "w") as f:
        f.write(report)

def main():
    parser = argparse.ArgumentParser(description="Analyze web agent evaluation results")
    parser.add_argument("--results_dir", type=str, default="results",
                        help="Directory containing results")
    parser.add_argument("--output_dir", type=str, default="analysis",
                        help="Directory to save analysis results")
    
    args = parser.parse_args()
    
    results = load_results(args.results_dir)
    generate_plots(results, args.output_dir)
    generate_report(results, args.output_dir)
    
    print(f"Analysis complete. Report saved to {os.path.join(args.output_dir, 'evaluation_report.md')}")

if __name__ == "__main__":
    main()
