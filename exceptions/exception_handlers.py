from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions import custom_exceptions

async def student_not_found_handler(
        request:Request,
        exc:custom_exceptions.StudentNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "detail":"Student not found"
        }
    ) 

async def student_already_exists_handler(
        request:Request,
        exc:custom_exceptions.StudentAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={
            "detail":"student already exists"
        }
    )

async def course_not_found_handler(
        request:Request,
        exc:custom_exceptions.CourseNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "detail":"Course not found"
        }
    ) 

async def course_already_exists_handler(
        request:Request,
        exc:custom_exceptions.CourseAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={
            "detail":"Course already exists"
        }
    )
async def enrollment_not_found_handler(
        request:Request,
        exc:custom_exceptions.EnrollmentNotFoundException
        ):
    return JSONResponse(
        status_code=404,
        content={"detail":"Enrollment  not found"}
    )


async def enrollment_already_exists_handler(
        request:Request,
        exc:custom_exceptions.EnrollmentAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={
            "detail":"Enrollment already exists"
        }
    )