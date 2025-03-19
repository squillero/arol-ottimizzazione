def tweaks(sol,s):
    new_sol=sol[:]
    for _ in range(s):
        i=int(np.random.randint(0,NUM_ITEMS-1))
        new_sol[i]=not new_sol[i]
    return new_sol
 
for mutstep in range(1,50+1):
    best_solution=initial_solution[:]
    tries=0
    last_try=0
    while tries<MAX_STEPS:
        tries+=1
        solution=tweaks(best_solution,2)
        if evaluate(solution)>evaluate(best_solution):
            last_try=tries
            best_solution=solution[:]
    ic(f"Mutstep: {mutstep} - At {last_try} tries, best value is {evaluate(best_solution)} for combination {best_solution}")