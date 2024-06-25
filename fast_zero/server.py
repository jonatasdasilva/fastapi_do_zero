#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API DO CURSO FASTAPI DO ZERO
Created By: Jônatas da Silva
Created Date: 24/06/2024
version=1.0

Description:
    - pt-br: A API do curso FASTAPI DO ZERO do canal
      do Eduardo Mendes.
    - en: .
"""

from fastapi import FastAPI

server = FastAPI()


@server.get('/', status_code=200)
def read_root():
    return {'message': 'Olá Mundo!'}
