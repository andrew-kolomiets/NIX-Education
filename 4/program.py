


input_list=['hqw price','wcwqdjncwd','qcwdcwqwdcprice']


output_list=[x.upper() if 'price' in x else x for x in input_list  ]

print(output_list)