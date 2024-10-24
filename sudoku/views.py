
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login


from django.shortcuts import render

from sudoku.sudoku_generator import SudokuGenerator


def solve_sudoku(request):
    generator = SudokuGenerator()  # Create a Sudoku generator instance
    puzzle = generator.generate(num_remove=50)  # Generate a Sudoku puzzle

    if request.method == 'POST':
        # Here, you would implement the logic to solve the Sudoku puzzle
        # You can retrieve user inputs from the request.POST and solve it.
        # For now, we will keep it simple and just return the generated puzzle.
        solution = None  # Replace this with the actual solving logic if implemented.

        return render(request, 'sudoku/solve.html', {'solution': solution, 'puzzle': puzzle})

    return render(request, 'sudoku/solve.html', {'puzzle': puzzle})


def home(request):
    return render(request, 'sudoku/home.html')  # Ensure this matches the location of home.html


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to a different page (e.g., home page)
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
