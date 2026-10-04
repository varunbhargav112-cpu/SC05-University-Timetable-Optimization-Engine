# Five Mandatory Test Cases

| Case | Setup | Expected behavior |
|---|---|---|
| Fixture 1 | 5 courses, 3 rooms, 10 slots | Feasible timetable should exist |
| Fixture 2 | Only one small room | Room shortage should be reported |
| Fixture 3 | Two courses, same faculty, same slot | Faculty clash detected |
| Fixture 4 | Two courses, same cohort, same slot | Cohort clash detected |
| Fixture 5 | Valid schedule outside preferred time | Soft penalty, not hard failure |
