#!/usr/bin/env python3
"""
Quick Stats Analysis for Messi's 800 Goals
==========================================
This script analyzes Lionel Messi's goal-scoring data from messi_goals.csv
and provides key statistics including total goals, top opponents, body part
distribution, and peak scoring year.

Author: Generated with Claude Code
"""

import csv
from collections import Counter
from datetime import datetime


def load_goals_data(filename='messi_goals.csv'):
    """
    Load goal data from CSV file.

    Args:
        filename: Path to the CSV file containing goal data

    Returns:
        List of dictionaries, each representing one goal
    """
    goals = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            goals.append(row)
    return goals


def get_total_goals(goals):
    """
    Calculate total number of goals.

    Args:
        goals: List of goal dictionaries

    Returns:
        Integer count of total goals
    """
    return len(goals)


def get_top_opponents(goals, top_n=5):
    """
    Find the opponents Messi scored most against.

    Args:
        goals: List of goal dictionaries
        top_n: Number of top opponents to return (default: 5)

    Returns:
        List of tuples (opponent_name, goal_count)
    """
    opponent_counter = Counter()
    for goal in goals:
        opponent = goal.get('opponent', 'Unknown')
        opponent_counter[opponent] += 1

    return opponent_counter.most_common(top_n)


def get_goals_by_body_part(goals):
    """
    Calculate goals scored with different body parts.

    Body part codes in dataset:
    1 = Right foot
    2 = Left foot
    3 = Head

    Args:
        goals: List of goal dictionaries

    Returns:
        Dictionary mapping body part names to goal counts
    """
    body_part_map = {
        '1': 'Right foot',
        '2': 'Left foot',
        '3': 'Head'
    }

    body_part_counter = Counter()
    for goal in goals:
        body_part_code = goal.get('body_part', '')
        body_part_name = body_part_map.get(body_part_code, 'Other')
        body_part_counter[body_part_name] += 1

    return dict(body_part_counter)


def get_peak_scoring_year(goals):
    """
    Find the year in which Messi scored the most goals.

    Args:
        goals: List of goal dictionaries

    Returns:
        Tuple of (year, goal_count)
    """
    year_counter = Counter()
    for goal in goals:
        date_str = goal.get('date', '')
        if date_str:
            # Parse date in format YYYY-MM-DD
            year = date_str.split('-')[0]
            year_counter[year] += 1

    if year_counter:
        peak_year, count = year_counter.most_common(1)[0]
        return (peak_year, count)
    return (None, 0)


def print_summary(goals):
    """
    Print a comprehensive summary of Messi's goal statistics.

    Args:
        goals: List of goal dictionaries
    """
    print("=" * 60)
    print("LIONEL MESSI - GOAL STATISTICS SUMMARY")
    print("=" * 60)
    print()

    # Total goals
    total = get_total_goals(goals)
    print(f"📊 TOTAL GOALS: {total}")
    print()

    # Top 5 opponents
    print("🎯 TOP 5 OPPONENTS:")
    print("-" * 40)
    top_opponents = get_top_opponents(goals, 5)
    for rank, (opponent, count) in enumerate(top_opponents, 1):
        print(f"  {rank}. {opponent:25s} {count:3d} goals")
    print()

    # Goals by body part
    print("⚽ GOALS BY BODY PART:")
    print("-" * 40)
    body_parts = get_goals_by_body_part(goals)
    # Sort by count descending
    sorted_body_parts = sorted(body_parts.items(), key=lambda x: x[1], reverse=True)
    for body_part, count in sorted_body_parts:
        percentage = (count / total) * 100
        print(f"  {body_part:15s} {count:3d} goals ({percentage:5.1f}%)")
    print()

    # Peak scoring year
    print("🏆 PEAK SCORING YEAR:")
    print("-" * 40)
    peak_year, peak_count = get_peak_scoring_year(goals)
    if peak_year:
        print(f"  {peak_year}: {peak_count} goals")
    print()

    print("=" * 60)


def main():
    """
    Main function to run the analysis.
    """
    try:
        # Load the data
        print("Loading data from messi_goals.csv...")
        goals = load_goals_data()
        print(f"Successfully loaded {len(goals)} goals!\n")

        # Print the summary
        print_summary(goals)

    except FileNotFoundError:
        print("Error: Could not find messi_goals.csv")
        print("Please ensure the file is in the same directory as this script.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
