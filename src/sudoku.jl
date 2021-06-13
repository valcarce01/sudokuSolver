using JuMP, GLPK
# Solving with optimization
sudoku=[4 6 0 0 9 0 0 0 0
        0 5 2 1 0 0 0 9 0
        0 0 0 2 3 0 5 0 0
        8 0 0 0 0 0 0 0 7
        0 0 0 0 2 0 0 0 8
        3 0 0 0 0 0 0 0 9
        0 0 0 5 1 0 8 0 0
        0 7 8 6 0 0 0 2 0
        6 1 0 0 8 0 0 0 0]
begin
sudoku = [3 0 4 0
    	  0 1 0 2
          0 4 0 3
          2 0 1 0]
# Creamos el modelo
model = Model(GLPK.Optimizer)
@variable(model, X[1:4, 1:4, 1:4], Bin)

@constraint(model, mapslices(sum, X, dims = (1, 2)) .== 1)
@constraint(model, mapslices(sum, X, dims = (1, 3)) .== 1)
@constraint(model, mapslices(sum, X, dims = (2, 3)) .== 1)
@constraint(model, sum(X[i:i+1, j:j+1, k] for k ∈ [1:4], i ∈ [1, 2], j ∈ [1, 2]) .== 1)
# Add the values
nonZeroIndices = findall(i -> i != 0, sudoku)
for i in nonZeroIndices
    @constraint(model, X[i, sudoku[i]] == 1)
end

@objective(model, Max, 0)
optimize!(model)
solution_summary(model)
end