from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates


# ============================================================
# ROUTER
# ============================================================

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


# ============================================================
# LOGIN PAGE
# ============================================================

@router.get("/login")
async def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "user": None,
            "error": None
        }
    )


# ============================================================
# LOGIN PROCESS
# ============================================================

@router.post("/login")
async def login_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):

    print("=" * 60)
    print("LOGIN REQUEST")
    print("Email:", email)
    print("Password received:", bool(password))
    print("=" * 60)

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not email.strip():

        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={
                "user": None,
                "error": "Please enter your email."
            },
            status_code=400
        )

    if not password.strip():

        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={
                "user": None,
                "error": "Please enter your password."
            },
            status_code=400
        )

    # --------------------------------------------------------
    # DEMO LOGIN
    # --------------------------------------------------------

    response = RedirectResponse(
        url="/dashboard/",
        status_code=303
    )

    response.set_cookie(
        key="user_email",
        value=email,
        httponly=True
    )

    print("LOGIN SUCCESS")
    print("Redirecting to dashboard...")
    print("=" * 60)

    return response


# ============================================================
# REGISTER PAGE
# ============================================================

@router.get("/register")
async def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={
            "user": None,
            "error": None
        }
    )


# ============================================================
# LOGOUT
# ============================================================

@router.get("/logout")
async def logout():

    response = RedirectResponse(
        url="/auth/login",
        status_code=303
    )

    response.delete_cookie("user_email")

    return response

