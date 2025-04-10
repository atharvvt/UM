from fastapi import APIRouter, HTTPException
from app.sb_client import supabase
from app.schemas.admin_schema import Main_Admin, Update_Main_Admin, Partner_Admin, Update_Partner_Admin

router = APIRouter()

@router.post("/add")
def add_main_admin(admin: Main_Admin):
    try:
        response = supabase.table('user_main_admin').insert({
            'name' : admin.name,
            'email' : admin.email,
            'user_id' : admin.user_id,
            'role' : 'main_admin'
        }).execute()
        return {"message": "Admin added", "data": response.data}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/edit/{email}")
def edit_main_admin(email: str, admin: Update_Main_Admin):
    try:
        update_data = {k: v for k, v in admin.dict().items() if v is not None}
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        response = supabase.table('user_main_admin').update(update_data).eq('email',email).execute()
        return {"message": f"Edited admin data: {response.data}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete/{email}")
def delete_main_admin(email: str):
    try:
        response = supabase.table("user_main_admin").delete().eq('email',email).execute()
        return {"message": f"Deleted admin {email}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



