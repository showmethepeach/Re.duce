# # DB Schema

- User
  - `username` : `UsernameField`
  - `password` : `CharField`
  - `phone_number` : `CharField`
  - `owner` : `OneToOneField` 불린값 체크 방법은 리서치 
  - `customer` : `OneToOneField` 불린값 체크 방법은 리서치 
- Owner
  - `name` : `CharField`


- Customer
- Shop
  - `name` : `CharField` 
  - `description` : `CharField` 
  - `business_number` : `CharField`
  - `contact_number` : `CharField`
  - `address` : `CharField`
  - `photo` : `ImageField` 
- Order
  - `customer` : `ForeignKey` `Customer` 
  - `shop` : `ForeignKey` `Shop`  
  - `total_price` : `IntegerField` 
  - `ordered_at` : `DateTimeField` 
- OrderSaleMenu
  - `order` : `ForeignKey` `Order` 
  - `menu` : `ForeignKey` `SaleMenu` 
  - `quantity` : `IntegerField`
- SaleMenu
  - `menu` : `OneToOneField` `Menu`
  - `sale_rate` : `IntegerField` 
  - `sale_price` : `IntegerField` 
- Menu
  - `shop` : `ForeignKey` `Shop`
  - `name` : `CharField` 
  - `price` : `IntegerField`
  - `description` : `TextField`
  - `photo` : `ImageField` 
  - `is_sale` : `BooleanField`  