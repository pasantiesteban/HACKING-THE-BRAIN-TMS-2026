# “Hacking the Brain”: Improving Coding Outcomes with Neurostimulation 

## Abstract
Can magnetically stimulating the brain improve
software engineering outcomes? Recent advances exploring the
neural correlates of coding tasks have opened the door for
studies investigating neurostimulation’s potential to improve
performance. We report the first study to find a uniform, positive
effect on programming from transcranial magnetic stimulation.
We apply intermittent Theta Burst Stimulation (iTBS) to n = 27
participants performing code synthesis and comprehension tasks
in a standard IDE. We find neurostimulation of a brain region
associated with working memory to be a statistically significant
factor (p < 0.024) in explaining method synthesis response times
compared to an active control (average correct time 86.2 s vs.
94.3 s). In addition, it improves average participant accuracy by
6% (p < 0.01, d = 0.131). That is, we find that neurostimulation
of working memory induces a statistically significant fixed effect
that improves programming performance, rather than a random
one that varies per person. In addition, our approach does not
use the expensive medical imaging localization required by prior
work. These causal findings help refine our understanding of the
cognition underlying software engineering. While preliminary,
these exciting results suggest that neurostimulation can positively
impact coding tasks, giving our community an additional, and
orthogonal, cognitive support to improve outcomes for practitioners.

## Description

This repository contains the statistical analysis replication package for our ICSE 2027 paper submission.

It includes the experimental stimuli, participant surveys, anonymized datasets, and the scripts used to reproduce the statistical analyses reported in the manuscript.

To facilitate reproduction, we provide both preprocessed datasets, which can be used directly with the analysis scripts, and the corresponding raw datasets.

## Getting Started

This repository is organized to help reviewers locate the materials most relevant to their evaluation.

* For researchers interested in reproducing or verifying the statistical analyses reported in the manuscript, we recommend starting with `data-analysis\`.
* For researchers interested in reviewing participant screening and eligibility, we recommend `surveys\`.
* For researchers interested in examining the raw data, field notes, or post-study responses, we recommend `data\`.
* For researchers interested in reviewing the experimental stimuli used in the study, we recommend `stimuli\`.

For your connivence, each folder contains another `README` document providing more details (and in some cases steps) on the material within said folder.

## Authors

Priscila Santiesteban (pasanti@umich.edu), Hammad Ahmad (hammada@andrew.cmu.edu), Madeline Endres (mendres@umass.edu), Westley Weimer (weimerw@umich.edu)


## License

This project is licensed under the GNU General Public License V3.0 - see the LICENSE.md file for details

