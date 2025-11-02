#!/usr/bin/env python3
"""
Compare GPT-4 vs GPT-5 collusion behavior across identical experimental conditions.

Analyzes how different LLM models behave in the same market scenarios.
"""
from collusion_detection import CollusionDetector
import os

def main():
    print("=" * 80)
    print("GPT-4 vs GPT-5 COMPARATIVE COLLUSION ANALYSIS")
    print("=" * 80)
    print()

    detector = CollusionDetector('../experiments/baseline/results')

    # Define experiments with both GPT-4 and GPT-5 results
    experiments = {
        'Experiment A (No Comm, With Trans)': {
            'gpt4': 'gpt4 - a.log',
            'gpt5': 'gpt5 - a.log',
        },
        'Experiment C (With Comm, No Trans)': {
            'gpt4': 'gpt4 - c.log',
            'gpt5': 'gpt5 - c.log',
        },
    }

    # Also analyze GPT-4 only experiments for context
    gpt4_only = {
        'Experiment B (No Comm, No Trans)': 'gpt4 - b.log',
        'Experiment D (With Comm, With Trans)': 'gpt4 - d.log',
    }

    print("Analyzing experiments with both GPT-4 and GPT-5...")
    print()

    results = {}

    # Analyze paired experiments
    for exp_name, files in experiments.items():
        print(f"  - {exp_name}")
        for model, filename in files.items():
            filepath = f'../experiments/baseline/results/{filename}'
            if not os.path.exists(filepath):
                print(f"    WARNING: {filepath} not found!")
                continue
            label = f"{exp_name} [{model.upper()}]"
            results[label] = detector.analyze_experiment(filepath)

    # Analyze GPT-4 only experiments
    print()
    print("Analyzing GPT-4 only experiments (for reference)...")
    for exp_name, filename in gpt4_only.items():
        filepath = f'../experiments/baseline/results/{filename}'
        if os.path.exists(filepath):
            print(f"  - {exp_name}")
            label = f"{exp_name} [GPT4]"
            results[label] = detector.analyze_experiment(filepath)

    print()
    print(f"Analyzed {len(results)} experiment runs")
    print()

    detector.results = results

    # Generate standard report
    print("=" * 80)
    print("STANDARD COLLUSION METRICS")
    print("=" * 80)
    print()

    report = detector.generate_report()
    print(report)

    # Generate comparative analysis
    print()
    print("=" * 80)
    print("GPT-4 vs GPT-5 COMPARATIVE ANALYSIS")
    print("=" * 80)
    print()

    # Compare Experiment A
    if 'Experiment A (No Comm, With Trans) [GPT4]' in results and \
       'Experiment A (No Comm, With Trans) [GPT5]' in results:
        print("EXPERIMENT A (No Communication, With Transparency):")
        print("-" * 80)

        gpt4_a = results['Experiment A (No Comm, With Trans) [GPT4]']
        gpt5_a = results['Experiment A (No Comm, With Trans) [GPT5]']

        print(f"  Collusion Score:")
        print(f"    GPT-4: {gpt4_a['collusion_score']:.2f}")
        print(f"    GPT-5: {gpt5_a['collusion_score']:.2f}")
        print(f"    Δ:     {gpt5_a['collusion_score'] - gpt4_a['collusion_score']:+.2f}")

        print(f"\n  Price Correlation:")
        print(f"    GPT-4: {gpt4_a['price_correlation']:.3f}")
        print(f"    GPT-5: {gpt5_a['price_correlation']:.3f}")
        print(f"    Δ:     {gpt5_a['price_correlation'] - gpt4_a['price_correlation']:+.3f}")

        print(f"\n  Within-Day Price Variance:")
        print(f"    GPT-4: ${gpt4_a['price_variance']['avg_price_diff']:.2f}")
        print(f"    GPT-5: ${gpt5_a['price_variance']['avg_price_diff']:.2f}")

        print(f"\n  Margin Stability:")
        avg_stab_4 = (gpt4_a['margin_stability']['w1_margin_stability'] +
                      gpt4_a['margin_stability']['w2_margin_stability']) / 2
        avg_stab_5 = (gpt5_a['margin_stability']['w1_margin_stability'] +
                      gpt5_a['margin_stability']['w2_margin_stability']) / 2
        print(f"    GPT-4: {avg_stab_4:.3f}")
        print(f"    GPT-5: {avg_stab_5:.3f}")

        print(f"\n  Change Points:")
        print(f"    GPT-4: {gpt4_a['change_points']['num_change_points']} behavioral shifts")
        print(f"    GPT-5: {gpt5_a['change_points']['num_change_points']} behavioral shifts")

        print()

    # Compare Experiment C
    if 'Experiment C (With Comm, No Trans) [GPT4]' in results and \
       'Experiment C (With Comm, No Trans) [GPT5]' in results:
        print("EXPERIMENT C (With Communication, No Transparency):")
        print("-" * 80)

        gpt4_c = results['Experiment C (With Comm, No Trans) [GPT4]']
        gpt5_c = results['Experiment C (With Comm, No Trans) [GPT5]']

        print(f"  Collusion Score:")
        print(f"    GPT-4: {gpt4_c['collusion_score']:.2f}")
        print(f"    GPT-5: {gpt5_c['collusion_score']:.2f}")
        print(f"    Δ:     {gpt5_c['collusion_score'] - gpt4_c['collusion_score']:+.2f}")

        print(f"\n  Price Correlation:")
        print(f"    GPT-4: {gpt4_c['price_correlation']:.3f}")
        print(f"    GPT-5: {gpt5_c['price_correlation']:.3f}")
        print(f"    Δ:     {gpt5_c['price_correlation'] - gpt4_c['price_correlation']:+.3f}")

        print(f"\n  Within-Day Price Variance:")
        print(f"    GPT-4: ${gpt4_c['price_variance']['avg_price_diff']:.2f}")
        print(f"    GPT-5: ${gpt5_c['price_variance']['avg_price_diff']:.2f}")

        print(f"\n  Margin Stability:")
        avg_stab_4 = (gpt4_c['margin_stability']['w1_margin_stability'] +
                      gpt4_c['margin_stability']['w2_margin_stability']) / 2
        avg_stab_5 = (gpt5_c['margin_stability']['w1_margin_stability'] +
                      gpt5_c['margin_stability']['w2_margin_stability']) / 2
        print(f"    GPT-4: {avg_stab_4:.3f}")
        print(f"    GPT-5: {avg_stab_5:.3f}")

        print(f"\n  Change Points:")
        print(f"    GPT-4: {gpt4_c['change_points']['num_change_points']} behavioral shifts")
        print(f"    GPT-5: {gpt5_c['change_points']['num_change_points']} behavioral shifts")

        print()

    # Key findings
    print("=" * 80)
    print("KEY FINDINGS")
    print("=" * 80)
    print()
    print("This analysis compares how GPT-4 and GPT-5 behave as market agents")
    print("under identical conditions.")
    print()
    print("Questions to investigate:")
    print("  1. Does GPT-5 show more/less collusive behavior than GPT-4?")
    print("  2. Are GPT-5 agents better at maintaining coordinated pricing?")
    print("  3. Do more advanced models detect and exploit coordination opportunities?")
    print("  4. Are temporal dynamics (change points) more stable with GPT-5?")
    print()

    # Save results
    output_dir = './outputs/gpt_comparison'
    detector.save_results(output_dir)

    print("=" * 80)
    print(f"Analysis complete! Results saved to: {output_dir}/")
    print("=" * 80)
    print()

if __name__ == '__main__':
    main()
