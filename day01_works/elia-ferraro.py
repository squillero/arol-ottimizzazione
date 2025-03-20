value_per_weight = VALUES / np.sum(WEIGHTS, axis=1)
sorted_indices = np.argsort(-value_per_weight)
 
def tweak(sol):
    new_sol = sol[:]
 
    for i in sorted_indices:
        if not new_sol[i]:
            new_sol[i] = True
            if fitness(new_sol) != -1:
                return new_sol
            new_sol[i] = False
 
    for i in reversed(sorted_indices):
        if new_sol[i]:
            new_sol[i] = False
            if fitness(new_sol) != -1:
                return new_sol
            new_sol[i] = True
           
    return new_sol
 
step = 0
best_solution = np.random.choice([True, False], size=NUM_ITEMS)
 
best_value = fitness(best_solution)
 
while step < MAX_STEPS:
    step += 1  
    solution = tweak(best_solution)
 
    if fitness(solution) > best_value:
        best_solution = solution[:]    
        best_value = fitness(best_solution)
   
ic(fitness(best_solution))