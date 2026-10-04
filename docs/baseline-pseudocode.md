# Baseline Pseudocode

1. READ one valid input row.
2. IF the row is invalid:
   - SHOW a clear error.
3. ELSE:
   - APPLY the simple baseline rules in order.
   - CALCULATE the baseline output.
   - PRINT the output and rule used.
   - SAVE the result for later comparison.

### Baseline rules
1. Read courses in file order.
2. Scan slots from first to last.
3. For each slot, scan compatible rooms.
4. Choose the first placement that causes no hard clash.
5. If no placement is possible, mark the course unplaced.
6. Count unplaced courses.
7. Count soft preference penalties.
