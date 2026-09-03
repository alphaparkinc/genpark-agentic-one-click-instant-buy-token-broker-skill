class AgenticOneClickInstantBuyTokenBrokerClient:
    def execute_instant_buy_transaction(self, merchant_id='mch_costco_9918', cart_items=[{'sku': 'SKU-ORGANIC-COFFEE-01', 'qty': 2, 'unit_price': 18.99}], encrypted_vault_buyer_token='tok_vault_enc_881273'):
        return {
            'instant_buy_order_id': 'buy_ord_7721',
            'merchant_id': merchant_id,
            'subtotal_usd': 37.98,
            'tax_and_shipping_usd': 4.50,
            'total_charged_usd': 42.48,
            'order_confirmation_code': 'GENPARK-INSTANT-7721',
            'settlement_status': 'PAID_SETTLED',
            'receipt_pdf_download_url': 'https://checkout.instant.genpark.ai/receipts/7721.pdf'
        }
