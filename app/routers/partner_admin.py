from fastapi import APIRouter, HTTPException
from app.sb_client import supabase
from app.schemas.admin_schema import Main_Admin, Update_Main_Admin, Partner_Admin, Update_Partner_Admin
from app.utils.security import hash_password
router = APIRouter()

@router.post("/add")
def add_partner_admin(admin: Partner_Admin):
    try:
        hashed_password = hash_password(admin.password)
        response = supabase.table('user_partner_admin').insert({
            'name': admin.name,
            'email': admin.email,
            'user_id': admin.user_id,
            'role': 'partner_admin',
            'password': hashed_password  # consider hashing in production
        }).execute()
        return {"message": "Partner admin added", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/edit/{email}")
def edit_partner_admin(email: str, admin: Update_Partner_Admin):
    try:
        update_data = {k: v for k, v in admin.dict().items() if v is not None}

        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")

        if "password" in update_data:
            update_data["password"] = hash_password(update_data["password"])

        response = supabase.table('user_partner_admin').update(update_data).eq('email', email).execute()
        return {"message": f"Edited partner admin data: {response.data}"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/delete/{email}")
def delete_partner_admin(email: str):
    try:
        response = supabase.table('user_partner_admin').delete().eq('email', email).execute()
        return {"message": f"Deleted partner admin {email}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))