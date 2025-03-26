#!/bin/bash

# Set variables
MODEL="gpt-4o"
MAX_SAMPLES=100  # Set to None for full evaluation

# Create directories
mkdir -p results
mkdir -p analysis

# Prepare datasets
echo "Preparing datasets..."
python prepare_datasets.py --datasets all

# Run evaluations for each benchmark
for benchmark in mind2web webarena webvoyager webcanvas
do
    echo "Running evaluation on $benchmark..."
    python run_evaluations.py --benchmark $benchmark --output_dir results --model $MODEL --max_samples $MAX_SAMPLES
done

# Analyze results
echo "Analyzing results..."
python analyze_results.py --results_dir results --output_dir analysis

echo "Evaluation complete! Results are in the 'results' directory and analysis in the 'analysis' directory."
