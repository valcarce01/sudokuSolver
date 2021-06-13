using GLPK: optimize!
using JuMP, GLPK
#### WORKING
model = Model(GLPK.Optimizer)
@variable(model, X[1:4, 1:4, 1:4], Bin)
@constraints(model, begin
    oneValuePerCell, sum(X[1:4, 1:4,k] for k ∈ 1:4) .== 1
    oneValuePerRow,  sum(X[1:4, j, 1:4] for j ∈ 1:4) .== 1
    oneValuePerColumn, sum(X[i, 1:4, 1:4] for i ∈ 1:4) .== 1
    oneValuePerBlock,  sum(X[i:i+1, j:j+1, k] for k ∈ [1:4], i ∈ [1, 3], j ∈ [1, 3]) .== 1
end)
# Add the values
nonZeroIndices = findall(i -> i != 0, sudoku)
for i in nonZeroIndices
    @constraint(model, X[i, sudoku[i]] == 1)
end
@objective(model, Max, 0)
optimize!(model)
#####
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

sudoku = [5 3 0 0 7 0 0 0 0
            6 0 0 1 9 5 0 0 0
            0 9 8 0 0 0 0 6 0
            8 0 0 0 6 0 0 0 3
            4 0 0 8 0 3 0 0 1
            7 0 0 0 2 0 0 0 6
            0 6 0 0 0 0 2 8 0
            0 0 0 4 1 9 0 0 5
            0 0 0 0 8 0 0 7 9]
#####################
n = 3
nn = 3^2
model = Model(GLPK.Optimizer)
@variable(model, X[1:nn, 1:nn, 1:nn], Bin)
@constraints(model, begin
    oneValuePerCell, sum(X[1:nn, 1:nn,k] for k ∈ 1:nn) .== 1
    oneValuePerRow,  sum(X[1:nn, j, 1:nn] for j ∈ 1:nn) .== 1
    oneValuePerColumn, sum(X[i, 1:nn, 1:nn] for i ∈ 1:nn) .== 1
    oneValuePerBlock,  sum(X[i:i+2, j:j+2, k] for k ∈ [1:nn], i ∈ [1, 4, 7], j ∈ [1, 4, 7]) .== 1
end)
# Add the values
nonZeroIndices = findall(i -> i != 0, sudoku)
for i in nonZeroIndices
    @constraint(model, X[i, sudoku[i]] == 1)
end
@objective(model, Max, 0)
optimize!(model)
solution_summary(model)