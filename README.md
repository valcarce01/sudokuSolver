# Sudoku solver
A simple soduko solver implementation. Works for easy sudokus, and it's its only intentios, as long as sudokus are a [NP-complete problem](https://en.wikipedia.org/wiki/NP-completeness). 

The solution implemented involves graphs and sets, i'll explain how it works with an exampleof a 4x4 (this solver is working only for a 9x9). Imagine this sudoku:



<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">4</th>
    <th class="tg-0pky"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">3</td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>


The first done is to asign a name to each cell, I decided to like:

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">A1</th>
    <th class="tg-c3ow">A2</th>
    <th class="tg-c3ow">A3</th>
    <th class="tg-c3ow">A4</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">B1</td>
    <td class="tg-c3ow">B2</td>
    <td class="tg-c3ow">B3</td>
    <td class="tg-c3ow">B4</td>
  </tr>
  <tr>
    <td class="tg-c3ow">C1</td>
    <td class="tg-c3ow">C2</td>
    <td class="tg-c3ow">C3</td>
    <td class="tg-c3ow">C4</td>
  </tr>
  <tr>
    <td class="tg-c3ow">D1</td>
    <td class="tg-c3ow">D2</td>
    <td class="tg-c3ow">D3</td>
    <td class="tg-c3ow">D4</td>
  </tr>
</tbody>
</table>

After that, it's created a graph (for after solving it), the graph has as vertices all the cells and, the edges, connect 2 vertices that can not have the same value. For example, in the table above, A1 can not have a value that is in A2, A3, A4, B1, C1, D1 or A4, as the rules for the sudoku does not allow to have the same values in rows, columns or squares. The graph seems to be something like this:

![alt text](https://github.com/valcarce01/sudokuSolver/blob/master/files/graph.PNG "Graph example of a 4x4 sudoku")

Each vertex will store its name and a set of values (the ones which it can have). For the vertices we know (given on the table before starting the game), we travel to all the vertices it's pointing to and do remove that posibility. 

The 'algorithm' just does what has been explained in loop (while removing numbers) and, when not adding, checks wheter it has already won; if not, bad luck, it's not planned to be able to try out the many (or not) possibilities that can actually handle.

Although it can not solve all sudokus, the ones it can, are solved in an average of less than 0.001 seconds, due to the fact of the graph implementation and working with numpy arrays (as matrix for the sudoku indexes values).

The code is provided of a pair of examples: a low-level one and a mid-level one.