from client import AgenticOneClickInstantBuyTokenBrokerClient

def main():
    client = AgenticOneClickInstantBuyTokenBrokerClient()
    res = client.execute_instant_buy_transaction('mch_target', [{'sku': 'SKU-01', 'qty': 1, 'unit_price': 25.00}], 'tok_123')
    print('Agentic Instant Buy Token Broker: ' + res['instant_buy_order_id'] + ' (' + res['order_confirmation_code'] + ')')
    print('Total Charged: $' + str(res['total_charged_usd']) + ' | Status: ' + res['settlement_status'])
    print('Receipt URL: ' + res['receipt_pdf_download_url'])

if __name__ == '__main__':
    main()
