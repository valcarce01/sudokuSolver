using GLPK, JuMP
@doc """
Solves sudoku as an optimization problem
"""
function optimization(A::Matrix; solver = GLPK.Optimizer)
    nn = size(A)[1]
    n = Int(sqrt(nn))

    # Create model for optimization with JuMP
    model = Model(solver)

    # Create the variables (binary)
    @variable(model, X[1:nn, 1:nn, 1:nn], Bin)

    # Start the constraints
    @constraints(model, begin
        oneKPerCell, sum(X[1:nn, 1:nn, k] for k ∈ 1:nn) .== 1
        oneKPerRow, sum(X[1:nn, j, 1:nn] for j ∈ 1:nn) .== 1
        oneKPerCol, sum(X[i, 1:nn, 1:nn] for i ∈ 1:nn) .== 1
        oneKPerBlock, sum.(X[i:i+n-1, j:j+n-1, k] for k ∈ 1:nn, i ∈ 1:n:nn, j ∈ 1:n:nn) .== 1
    end)

    # Add the values
    nonZeroIndices = findall(i -> i != 0, A)
    for i in nonZeroIndices
        @constraint(model, X[i, A[i]] == 1)
    end

    # @objective(model, Max, 0) # there nothing to optimize 

    optimize!(model)
    
    M = zeros(nn, nn)
    if Int(termination_status(model)) == 1
        # We should build the sudoku
        return Int.(sum(value.(X[:,:,k]) * k for k in 1:nn))
    else
        @warn("No solution found")
    end
end