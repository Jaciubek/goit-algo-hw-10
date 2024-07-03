import pulp

# Defining the problem
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Defining the decision variables
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Continuous')

# Defining the constraints
prob += 2 * lemonade + 1 * fruit_juice <= 100  # Water constraint
prob += 1 * lemonade <= 50                     # Sugar constraint
prob += 1 * lemonade <= 30                     # Lemon Juice constraint
prob += 2 * fruit_juice <= 40                  # Fruit Puree constraint

# Defining the objective function
prob += lemonade + fruit_juice

# Solving the problem
prob.solve()

# Print the results
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Optimal number of Lemonade to produce: {pulp.value(lemonade)}")
print(f"Optimal number of Fruit Juice to produce: {pulp.value(fruit_juice)}")
print(f"Max production: {pulp.value(prob.objective)}")