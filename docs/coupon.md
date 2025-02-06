# Coupon
Couponは支払い時に指定し、支払い処理の前にCouponに指定の方法で値引き処理を行います。
Couponは特定店舗で利用できるものや利用可能期間、配信条件などを設定できます。


<a name="list-coupons"></a>
## ListCoupons: クーポン一覧の取得
指定したマネーのクーポン一覧を取得します

```PYTHON
response = client.send(pp.ListCoupons(
                          "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",               # private_money_id: 対象クーポンのマネーID
                          coupon_id="lp3S7",                                    # クーポンID
                          coupon_name="MyfZK",                                  # クーポン名
                          issued_shop_name="P",                                 # 発行店舗名
                          available_shop_name="biZ1Lwce18",                     # 利用可能店舗名
                          available_from="2023-10-12T06:08:37.000000Z",         # 利用可能期間 (開始日時)
                          available_to="2020-10-23T05:13:32.000000Z",           # 利用可能期間 (終了日時)
                          page=1,                                               # ページ番号
                          per_page=50                                           # 1ページ分の取得数
))
```



### Parameters
**`private_money_id`** 
  

対象クーポンのマネーIDです(必須項目)。
存在しないマネーIDを指定した場合はprivate_money_not_foundエラー(422)が返ります。


```json
{
  "type": "string",
  "format": "uuid"
}
```

**`coupon_id`** 
  

指定されたクーポンIDで結果をフィルターします。
部分一致(前方一致)します。


```json
{
  "type": "string"
}
```

**`coupon_name`** 
  

指定されたクーポン名で結果をフィルターします。


```json
{
  "type": "string"
}
```

**`issued_shop_name`** 
  

指定された発行店舗で結果をフィルターします。


```json
{
  "type": "string"
}
```

**`available_shop_name`** 
  

指定された利用可能店舗で結果をフィルターします。


```json
{
  "type": "string"
}
```

**`available_from`** 
  

利用可能期間でフィルターします。フィルターの開始日時をISO8601形式で指定します。


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`available_to`** 
  

利用可能期間でフィルターします。フィルターの終了日時をISO8601形式で指定します。


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`page`** 
  

取得したいページ番号です。

```json
{
  "type": "integer",
  "minimum": 1
}
```

**`per_page`** 
  

1ページ分の取得数です。デフォルトでは 50 になっています。

```json
{
  "type": "integer",
  "minimum": 1
}
```



成功したときは
[PaginatedCoupons](./responses.md#paginated-coupons)
を返します

### Error Responses
|status|type|ja|en|
|---|---|---|---|
|403|unpermitted_admin_user|この管理ユーザには権限がありません|Admin does not have permission|
|422|shop_user_not_found|店舗が見つかりません|The shop user is not found|
|422|private_money_not_found|マネーが見つかりません|Private money not found|



---


<a name="create-coupon"></a>
## CreateCoupon: クーポンの登録
新しいクーポンを登録します

```PYTHON
response = client.send(pp.CreateCoupon(
                          "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                          "q5OqWuTabdRaaHOyfGqVUncXzhjskeGyZxmbEy050Zlv3tzVr8aTPDqMKbxS0Vs3OlIrdn",
                          "2024-08-18T06:06:48.000000Z",
                          "2024-05-17T12:55:19.000000Z",
                          "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",               # issued_shop_id: 発行元の店舗ID
                          description="U9Fte9Z959oBy13mtel3d8TfJ3Ol39ScasZnA58jo0hnztlMdM7BVfn4iFYyJJXfrDUn2Z5dTBMhYMOaLFSQqsldJHk3l4cpZ7fJl29A3O6y0fQnXOgwkIth5yMWiTVYzb9YasuIp7v4EzACicWq4Ul0bBBFnJwjrPufrwL5Z4qM5cyeftMbZhJuNsCdqVbAgLZQKQXblhvdQVC38rMOaKHSf5htPpycWdWsbduWBxtfg1Kliu4",
                          discount_amount=2880,
                          discount_percentage=2445.0,
                          discount_upper_limit=5047,
                          display_starts_at="2023-06-11T04:31:55.000000Z",      # クーポンの掲載期間(開始日時)
                          display_ends_at="2024-10-29T08:09:45.000000Z",        # クーポンの掲載期間(終了日時)
                          is_disabled=True,                                     # 無効化フラグ
                          is_hidden=False,                                      # クーポン一覧に掲載されるかどうか
                          is_public=True,                                       # アプリ配信なしで受け取れるかどうか
                          code="pvwbo",                                         # クーポン受け取りコード
                          usage_limit=6198,                                     # ユーザごとの利用可能回数(NULLの場合は無制限)
                          min_amount=433,                                       # クーポン適用可能な最小取引額
                          is_shop_specified=True,                               # 特定店舗限定のクーポンかどうか
                          available_shop_ids=["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], # 利用可能店舗リスト
                          storage_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"     # ストレージID
))
```

`is_shop_specified`と`available_shop_ids`は同時に指定する必要があります。


### Parameters
**`private_money_id`** 
  


```json
{
  "type": "string",
  "format": "uuid"
}
```

**`name`** 
  


```json
{
  "type": "string",
  "maxLength": 128
}
```

**`description`** 
  


```json
{
  "type": "string",
  "maxLength": 256
}
```

**`discount_amount`** 
  


```json
{
  "type": "integer",
  "minimum": 0
}
```

**`discount_percentage`** 
  


```json
{
  "type": "number",
  "minimum": 0
}
```

**`discount_upper_limit`** 
  


```json
{
  "type": "integer",
  "minimum": 0
}
```

**`starts_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`ends_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`display_starts_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`display_ends_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`is_disabled`** 
  


```json
{
  "type": "boolean"
}
```

**`is_hidden`** 
  

アプリに表示されるクーポン一覧に掲載されるかどうか。
主に一時的に掲載から外したいときに用いられる。そのためis_publicの設定よりも優先される。


```json
{
  "type": "boolean"
}
```

**`is_public`** 
  


```json
{
  "type": "boolean"
}
```

**`code`** 
  


```json
{
  "type": "string"
}
```

**`usage_limit`** 
  


```json
{
  "type": "integer"
}
```

**`min_amount`** 
  


```json
{
  "type": "integer"
}
```

**`issued_shop_id`** 
  


```json
{
  "type": "string",
  "format": "uuid"
}
```

**`is_shop_specified`** 
  


```json
{
  "type": "boolean"
}
```

**`available_shop_ids`** 
  


```json
{
  "type": "array",
  "items": {
    "type": "string",
    "format": "uuid"
  }
}
```

**`storage_id`** 
  

Storage APIでアップロードしたクーポン画像のStorage IDを指定します

```json
{
  "type": "string",
  "format": "uuid"
}
```



成功したときは
[CouponDetail](./responses.md#coupon-detail)
を返します

### Error Responses
|status|type|ja|en|
|---|---|---|---|
|400|invalid_parameters|項目が無効です|Invalid parameters|
|403|unpermitted_admin_user|この管理ユーザには権限がありません|Admin does not have permission|
|404|partner_storage_not_found|指定したIDのデータは保存されていません|Not found by storage_id|
|422|shop_user_not_found|店舗が見つかりません|The shop user is not found|
|422|private_money_not_found|マネーが見つかりません|Private money not found|
|422|coupon_image_storage_conflict|クーポン画像のストレージIDは既に存在します|The coupon image storage_id is already exists|



---


<a name="get-coupon"></a>
## GetCoupon: クーポンの取得
指定したIDを持つクーポンを取得します

```PYTHON
response = client.send(pp.GetCoupon(
                          "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"                # coupon_id: クーポンID
))
```



### Parameters
**`coupon_id`** 
  

取得するクーポンのIDです。
UUIDv4フォーマットである必要があり、フォーマットが異なる場合は InvalidParametersエラー(400)が返ります。
指定したIDのクーポンが存在しない場合はCouponNotFoundエラー(422)が返ります。

```json
{
  "type": "string",
  "format": "uuid"
}
```



成功したときは
[CouponDetail](./responses.md#coupon-detail)
を返します



---


<a name="update-coupon"></a>
## UpdateCoupon: クーポンの更新
指定したクーポンを更新します

```PYTHON
response = client.send(pp.UpdateCoupon(
                          "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",               # coupon_id: クーポンID
                          name="0xPHohZAf",
                          description="XS5WAq97VI0kJjyO9S00lRKqhRSKyv4aeUNiX5kIXisF2lvLdWFAH9CECfmZyvOgcw2bcIoYI3B409EBsOM5mHn7CA1SM3xNEFCgQheyCbSnP7P0SqnjQBF0gNpyvaB",
                          discount_amount=3040,
                          discount_percentage=5882.0,
                          discount_upper_limit=6683,
                          starts_at="2023-09-20T07:37:14.000000Z",
                          ends_at="2020-03-18T12:34:52.000000Z",
                          display_starts_at="2022-11-10T14:34:49.000000Z",      # クーポンの掲載期間(開始日時)
                          display_ends_at="2024-10-22T01:57:25.000000Z",        # クーポンの掲載期間(終了日時)
                          is_disabled=True,                                     # 無効化フラグ
                          is_hidden=False,                                      # クーポン一覧に掲載されるかどうか
                          is_public=True,                                       # アプリ配信なしで受け取れるかどうか
                          code="X",                                             # クーポン受け取りコード
                          usage_limit=4412,                                     # ユーザごとの利用可能回数(NULLの場合は無制限)
                          min_amount=2773,                                      # クーポン適用可能な最小取引額
                          is_shop_specified=False,                              # 特定店舗限定のクーポンかどうか
                          available_shop_ids=["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], # 利用可能店舗リスト
                          storage_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"     # ストレージID
))
```


`discount_amount`と`discount_percentage`の少なくとも一方は指定する必要があります。



### Parameters
**`coupon_id`** 
  


```json
{
  "type": "string",
  "format": "uuid"
}
```

**`name`** 
  


```json
{
  "type": "string",
  "maxLength": 128
}
```

**`description`** 
  


```json
{
  "type": "string",
  "maxLength": 256
}
```

**`discount_amount`** 
  


```json
{
  "type": "integer",
  "minimum": 0
}
```

**`discount_percentage`** 
  


```json
{
  "type": "number",
  "minimum": 0
}
```

**`discount_upper_limit`** 
  


```json
{
  "type": "integer",
  "minimum": 0
}
```

**`starts_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`ends_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`display_starts_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`display_ends_at`** 
  


```json
{
  "type": "string",
  "format": "date-time"
}
```

**`is_disabled`** 
  


```json
{
  "type": "boolean"
}
```

**`is_hidden`** 
  

アプリに表示されるクーポン一覧に掲載されるかどうか。
主に一時的に掲載から外したいときに用いられる。そのためis_publicの設定よりも優先される。


```json
{
  "type": "boolean"
}
```

**`is_public`** 
  


```json
{
  "type": "boolean"
}
```

**`code`** 
  


```json
{
  "type": "string"
}
```

**`usage_limit`** 
  


```json
{
  "type": "integer"
}
```

**`min_amount`** 
  


```json
{
  "type": "integer"
}
```

**`is_shop_specified`** 
  


```json
{
  "type": "boolean"
}
```

**`available_shop_ids`** 
  


```json
{
  "type": "array",
  "items": {
    "type": "string",
    "format": "uuid"
  }
}
```

**`storage_id`** 
  

Storage APIでアップロードしたクーポン画像のStorage IDを指定します

```json
{
  "type": "string",
  "format": "uuid"
}
```



成功したときは
[CouponDetail](./responses.md#coupon-detail)
を返します



---



