#!python3
import akshare as ak

def get_stock_zh_a_spot():
  '''
  获取A股实时行情数据

  该函数调用akshare库的stock_zh_a_spot方法获取A股实时行情数据，
  并将结果保存到Excel文件中。
  '''
  # 调用akshare库的stock_zh_a_spot方法获取A股实时行情数据
  stock_zh_a_spot_df = ak.stock_zh_a_spot()
  # 将结果保存到Excel文件中
  stock_zh_a_spot_df.to_excel('./files/a股列表.xlsx', index=False)
  print('数据已成功保存到 a股列表.xlsx 文件中')


def get_stock_zh_a_cyq_em(code):
  if not code:
    raise RuntimeError('请输入股票代码')
  stock_cyq_em_df = ak.stock_cyq_em(symbol=code, adjust='')
  stock_cyq_em_df.to_excel('./files/筹码分布数据.xlsx', index=False)
  print('筹码分布数据已保存到 筹码分布数据.xlsx文件中')

