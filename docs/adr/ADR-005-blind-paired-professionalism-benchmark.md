# ADR-005: Blind paired professionalism benchmark

- Status: accepted
- Date: 2026-08-11

## Context

The existing writing evaluation detects explicit fact, number, scope, and
forbidden-claim failures. It cannot determine whether prose is professionally
organized, uses conventional technical collocations, or improves because of the
library rather than because the underlying model is strong.

Reference-answer similarity is a poor oracle because many excellent paper
sentences are valid, and storing preferred answers would encourage imitation and
benchmark leakage. An unblinded single score would also confound treatment
identity with reviewer expectations.

## Decision

Evaluate identical writing tasks under two conditions: the same model without
library access and the same model with a pinned Super Library revision. Randomize
pair order and A/B side, keep the mapping in a checksum-bound private key, and
require independent raters to score each response before choosing a preference.

Combine three non-substitutable evidence layers:

1. deterministic case invariants for facts and prohibited assertions;
2. six anchored human professionalism dimensions plus critical-error flags; and
3. paired effect estimates, preference, bootstrap uncertainty, and rater
   agreement.

The configured thresholds are operational release gates, not a universal
definition of publishable prose. A result applies only to its pinned task suite,
model revision, generation parameters, library commit, and raters.

## Consequences

- The project can measure both absolute readiness and incremental library value.
- Raters never need access to hidden retrieval IDs or condition labels.
- A polished response with a scientific critical error cannot pass by averaging
  style scores.
- Full runs require manual effort from at least two qualified raters.
- The benchmark does not prove scientific truth, venue acceptance, or
  generalization to unsampled manuscripts.
