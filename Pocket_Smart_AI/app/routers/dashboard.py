from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import init_db, get_all_expenses, add_expense_db, delete_expense_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Initialize database table
init_db()

@router.get("")
@router.get("/")
async def get_dashboard(request: Request):
    user_email = request.cookies.get("user_email", "user@pocketsmart.ai")
    
    expenses_db = get_all_expenses()
    total_budget = 15000.0
    total_spent = sum(float(item.get("amount", 0)) for item in expenses_db)
    remaining_balance = total_budget - total_spent

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user_email": user_email,
            "expenses": expenses_db,
            "total_spent": total_spent,
            "remaining_balance": remaining_balance,
            "total_budget": total_budget
        }
    )

@router.post("/add-expense")
async def add_expense(title: str = Form(...), amount: float = Form(...)):
    add_expense_db(title, amount)
    return RedirectResponse(url="/dashboard", status_code=303)

@router.post("/delete-expense")
async def delete_expense(expense_id: int = Form(...)):
    delete_expense_db(expense_id)
    return RedirectResponse(url="/dashboard", status_code=303)

