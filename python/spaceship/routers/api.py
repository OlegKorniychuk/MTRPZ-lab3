from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
def multiplyMatrixes() -> dict:
  firstMatrix = np.random.rand(10, 10)
  secondMatrix = np.random.rand(10, 10)

  resultMatrix = np.dot(firstMatrix, secondMatrix)

  response = {
    "matrix_a": firstMatrix.tolist(),
    "matrix_b": secondMatrix.tolist(),
    "product": resultMatrix.tolist()
  }

  return response
