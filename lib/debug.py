#!/usr/bin/env python3

from sqlalchemy import create_engine
from seed import engine,session

from models import Company, Dev,Freebie


print("\n Interactive Debug Mode. You can now test your models.")

if __name__ == '__main__':
    
    import ipdb; ipdb.set_trace()
