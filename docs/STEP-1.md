# Step 1 Project Contract

## Team and responsibilities
- Member 1 - Repository and Testing/UI
- Member 2 - Data
- Member 3 - Baseline
- Member 4 - Testing/UI

## One-sentence problem
Place courses into rooms and time slots without faculty, room, or cohort clashes.

## User of the product
A timetable coordinator who needs a clash-free weekly schedule.

## Inputs and units

| Field | Meaning | Type | Unit / allowed values |
|---|---|---|---|
| course_id | Course code | text | C01–C05 |
| cohort_id | Student group | text | G1/G2 |
| faculty_id | Teacher code | text | F1–F3 |
| weekly_sessions | Sessions required | integer | 1–4 |
| duration_slots | Session length | integer | 1 or 2 slots |
| required_room_type | Required room category | category | classroom/lab |
| room_id | Room identifier | text | R01–R03 |
| capacity | Room capacity | integer | > 0 |
| slot_id | Teaching slot | text | S01–S10 |
| day | Day | text | Monday–Friday |
| time | Time | text | Named time slot |

## Outputs and units
- course_id
- room_id
- slot_id
- faculty_id
- cohort_id
- hard-violation count
- soft-penalty count

## Baseline method
Read courses in file order. For each course, scan slots from first to last and choose the first room/slot that does not create a hard clash. If no placement is possible, mark the course unplaced. Count unplaced courses and preference penalties.

## Soft Computing method for M1
A Genetic Algorithm timetable for a small test case, compared with random or greedy placement.

## Advanced method for M2
Add more objectives and constraints, test larger cases, improve the interface, and deploy it.

## Dataset/scenario sources
The Step 1 dataset is a simulated educational fixture created for this project. It is not claimed to be real university data.

## Five mandatory test cases
1. Fixture 1: 5 courses, 3 rooms, 10 slots — feasible timetable should exist.
2. Fixture 2: one small room — room shortage should be reported.
3. Fixture 3: two courses, same faculty, same slot — faculty clash should be detected.
4. Fixture 4: two courses, same cohort, same slot — cohort clash should be detected.
5. Fixture 5: valid schedule outside preferred time — soft penalty, not hard failure.

## Product V1 screen sketch
See `docs/product-v1-sketch.png`.

## Risks and assumptions
- Data is simulated for Step 1.
- Room capacity must be greater than zero.
- IDs must be unique.
- Room type must match the course requirement.
- The first version uses simple validation and baseline rules.
- Preference penalties are treated as soft constraints.

## Step 1 completion evidence
- Validation source: `src/validate_data.py`
- Input data: `data/`
- Baseline pseudocode: `docs/baseline-pseudocode.md`
- Product sketch: `docs/product-v1-sketch.png`
- Results/evidence: `results/step1/`
