import pathlib, sys
sys.path.append(str(pathlib.Path('.').resolve()))
from app.repositories.csv_repository import ProductRepository_csv
from app.models.product import Product

repo = ProductRepository_csv('data/products.csv')
p = Product(id=1, name='Exemplo', desc='descricao', amount=5, price=9.99, created_at='2026-02-28', updated_at='2026-02-28')
repo.save_products([p])
print('Saved to', repo.file_path)
with open(repo.file_path, 'r', encoding='utf-8') as f:
    print(f.read())
