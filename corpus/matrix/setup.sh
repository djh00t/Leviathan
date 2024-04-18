#!/bin/bash

# Directories
DATA_DIR="data"
USER_REQUESTS_DIR="user-requests"

# Ensure directories exist
mkdir -p "$DATA_DIR"
mkdir -p "$USER_REQUESTS_DIR"

# Array of diagram types
declare -a diagram_types=(
  "block-diagram"
  "c4-diagram"
  "class-diagram"
  "entity-relationship-diagram"
  "flowchart"
  "gantt-chart"
  "gitgraph-diagram"
  "mindmaps"
  "pie-chart"
  "quadrant-chart"
  "requirement-diagram"
  "sankey"
  "sequence-diagram"
  "state-diagram"
  "timeline"
  "user-journey"
  "xy-chart"
  "zenuml-diagram"
)

# Function to fix and create files
fix_and_create_files() {
  local dir="$1"
  local prefix="$2"
  local suffix="$3"
  local extension="$4"

  for type in "${diagram_types[@]}"; do
    for i in {1..3}; do
      # Correct and incorrect file names
      local correct_file="${dir}/${type}${prefix}${i}${suffix}.${extension}"
      local incorrect_file="${dir}/${type}${prefix}.${i}${suffix}.${extension}"

      # Remove incorrect file if exists
      if [ -f "$incorrect_file" ]; then
        echo "Removing incorrect file: $incorrect_file"
        rm "$incorrect_file"
      fi

      # Create correct file if it does not exist
      if [ ! -f "$correct_file" ]; then
        echo "Creating correct file: $correct_file"
        touch "$correct_file"
      fi
    done
  done
}

# Fix and create dataset files in data directory
fix_and_create_files "$DATA_DIR" "-dataset-" "" "md"

# Fix and create user request files in user-requests directory
fix_and_create_files "$USER_REQUESTS_DIR" "-user-" "" "md"

echo "Setup and cleanup complete."
