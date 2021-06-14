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

s = [5 3 0 0 7 0 0 0 0
            6 0 0 1 9 5 0 0 0
            0 9 8 0 0 0 0 6 0
            8 0 0 0 6 0 0 0 3
            4 0 0 8 0 3 0 0 1
            7 0 0 0 2 0 0 0 6
            0 6 0 0 0 0 2 8 0
            0 0 0 4 1 9 0 0 5
            0 0 0 0 8 0 0 7 9]
#####################
sudoku = [3 4 1 0
          0 2 0 0
          0 0 2 0
          0 1 4 3]
n = 2
nn = n^2
model = Model(GLPK.Optimizer)
@variable(model, X[1:nn, 1:nn, 1:nn], Bin)
@constraints(model, begin
    oneValuePerCell, sum(X[1:nn, 1:nn,k] for k ∈ 1:nn) .== 1
    oneValuePerRow,  sum(X[1:nn, j, 1:nn] for j ∈ 1:nn) .== 1
    oneValuePerColumn, sum(X[i, 1:nn, 1:nn] for i ∈ 1:nn) .== 1
    oneValuePerBlock,  sum(X[i:i+1, j:j+1, k] for k ∈ [1:nn], i ∈ 1:n:nn, j ∈ 1:n:nn) .== 1
end)
# Add the values
nonZeroIndices = findall(i -> i != 0, sudoku)
for i in nonZeroIndices
    @constraint(model, X[i, sudoku[i]] == 1)
end
@objective(model, Max, 0)
optimize!(model)
solution_summary(model)

##########################
puzz1 = [
9  3  0  0  0  0  0  4  0
0  0  0  0  4  2  0  9  0
8  0  0  1  9  6  7  0  0
0  0  0  4  7  0  0  0  0
0  2  0  0  0  0  0  6  0
0  0  0  0  2  3  0  0  0
0  0  8  5  3  1  0  0  2
0  9  0  2  8  0  0  0  0
0  7  0  0  0  0  0  5  3
];

puzz2 = [
0  0  9  0  1  0  0  6  0
0  0  0  0  6  7  0  0  3
0  3  5  0  0  0  0  0  0
3  0  0  0  0  2  0  0  0
5  1  7  0  0  0  2  3  4
0  0  0  3  0  0  0  0  7
0  0  0  0  0  0  9  1  0
1  0  0  6  8  0  0  0  0
0  7  0  0  3  0  5  0  0
];

puzz3 = [
0  3  7  8  6  0  0  4  0
0  0  6  0  0  7  0  0  0
0  2  0  0  3  0  0  0  6
0  8  0  2  0  0  0  0  0
9  0  0  0  0  0  0  0  1
0  0  0  0  0  6  0  9  0
5  0  0  0  7  0  0  3  0
0  0  0  3  0  0  8  0  0
0  1  0  0  8  4  2  6  0
];


"""
`sudoku(A::Matrix)` solves the Sudoku puzzle given by the matrix `A`.
Here `A` is a 9-by-9 integer matrix whose nonzero entries are the
given values of a Sudoku puzzle and whose zero values are the blanks.
"""
function sudoku(A::Matrix{Int})
    n = 9
    nn = 3
    MOD = Model(GLPK.Optimizer)

    # variable X[i,j,k] = 1 means there's a k in cell (i,j)
    @variable(MOD,X[1:n,1:n,1:n], Bin)

    # At most one entry in each cell
    for i=1:n
        for j=1:n
            @constraint(MOD, sum(X[i,j,k] for k=1:n) == 1)
        end
    end

    # There is exactly one k in every row
    for i=1:n
        for k=1:n
            @constraint(MOD, sum(X[i,j,k] for j=1:n)==1)
        end
    end

    # There is exactly one k in every column
    for j=1:n
        for k=1:n
            @constraint(MOD, sum(X[i,j,k] for i=1:n)==1)
        end
    end

    # Each 3x3 sub square has exactly one k

    for a=1:nn
        for b=1:nn
            for k=1:n
                @constraint(MOD, sum(X[i,j,k] for i=3a-2:3a for j=3b-2:3b) == 1)
            end
        end
    end

    # Process values in A
    for i=1:n
        for j=1:n
            if A[i,j] != 0
                @constraint(MOD, X[i,j,A[i,j]] == 1)
            end
        end
    end

    # now solve and extract the solution
    optimize!(MOD)
    status = Int(termination_status(MOD))
    if status != 1
        error("No solution to this Sudoku puzzle")
    end

    XX = value.(X)
    B = zeros(Int,n,n)
    for i=1:n
        for j=1:n
            for k=1:n
                if XX[i,j,k]>0
                    B[i,j] = k
                end
            end
        end
    end
    return B
end