import pandas as pd
# import os
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
# from statistics import median
# from sklearn.linear_model import LinearRegression

df_range = pd.read_excel(r'Copy of AP Data Collection_Analysis.xlsx')

df_2019 = pd.read_excel(
    r'Copy of AP Data Collection Sheet.xlsx', sheet_name='Main Sheet')
df_2018 = pd.read_excel(
    r'Copy of AP Data Collection Sheet.xlsx', sheet_name='Data FY18-19')
df_2017 = pd.read_excel(
    r'Copy of AP Data Collection Sheet.xlsx', sheet_name='Data FY17-18')
df_2016 = pd.read_excel(
    r'Copy of AP Data Collection Sheet.xlsx', sheet_name='Data FY16-17')
df_2011 = pd.read_excel(r'Copy of AP ULB Data for Dashboard.xlsx')
# prefixes = list(df['Ulb Code'])
# suffixes = list(df['File Storeid'])
# for i in range(0, len(suffixes)):
#     suffixes[i] = suffixes[i].strip()
# complaint = list(df['Complaint Type'])
# for i in range(0, len(complaint)):
#     complaint[i] = complaint[i].strip()

df_range = df_range.loc[:, ~df_range.columns.str.contains('^Unnamed')]
df_range = df_range.replace('#DIV/0!', 0)
df_range = df_range.fillna(0)
df_2019 = df_2019.loc[:, ~df_2019.columns.str.contains('^Unnamed')]
df_2019 = df_2019.replace('#DIV/0!', 0)
df_2019 = df_2019.fillna(0)
df_2018 = df_2018.loc[:, ~df_2018.columns.str.contains('^Unnamed')]
df_2018 = df_2018.replace('#DIV/0!', 0)
df_2018 = df_2018.fillna(0)
df_2017 = df_2017.loc[:, ~df_2017.columns.str.contains('^Unnamed')]
df_2017 = df_2017.replace('#DIV/0!', 0)
df_2017 = df_2017.fillna(0)
df_2016 = df_2016.loc[:, ~df_2016.columns.str.contains('^Unnamed')]
df_2016 = df_2016.replace('#DIV/0!', 0)
df_2016 = df_2016.fillna(0)

# print(df.columns)

df_2019corp = df_2019[df_2019['ULB Type'] == 'Corp']
df_2018corp = df_2018[df_2018['ULB Type'] == 'Corp']
df_2017corp = df_2017[df_2017['ULB Type'] == 'Corp']
df_2016corp = df_2016[df_2016['ULB Type'] == 'Corp']
# print((df_2016corp['Regular ']+df_2016corp['Contract']).sum())
# print((df_2017corp['Regular ']+df_2017corp['Contract']).sum())
# print((df_2018corp['Regular ']+df_2018corp['Contract']).sum())
# print((df_2019corp['Regular']+df_2019corp['Contract']).sum())
# plt.plot(
#     ['2016', '2017', '2018', '2019'],
#     [df_2016corp['Annual Demand (FY17)\n[Excluding arrear/penalty]']/(100000*df_2016corp['Revenue']), df_2017corp['Annual Demand (FY18)\n[Excluding arrear/penalty]']/(100000*df_2017corp['Revenue']), df_2018corp['Annual Demand (FY19)\n[Excluding arrear/penalty]']/(100000*df_2018corp['Revenue']), df_2019corp['Annual Demand (FY19)\n[Excluding arrear/penalty]']/(100000*df_2019corp['Revenue'])], '--')
# plt.legend(df_2019corp['ULB Name'])
# plt.show()
# df_range = df_range.drop('ULB Type', axis=1)
# df_range = df_range.drop('District Name', axis=1)
# df_range = df_range.drop('Region', axis=1)
df_range = df_range. sort_values(by='ULB Population', ascending=True)

for i in df_range.columns:
    w, h = figaspect(1/3)
    fig, ax = plt.subplots(figsize=(w, h))
    pop_ranges = [
        'Less than 50k',
        '50k to 1 Lac',
        '1 Lac to 2 Las',
        '2 Lacs to 3 Lacs',
        '3 Lacs to 5 Lacs',
        '5 Lacs to 10 Lacs',
        '10 Lacs to 20 Lacs',
        '20 Lacs to 30 Lacs']
    plt.ylabel(i)
    plt.grid(axis='y')
    # if (i != 'ULB Name' and i != 'Population Range'):
    #     print(i)
    #     plt.ylim(top=3*median(df_range[i]))
    for j in pop_ranges:
        df_range_x = df_range[df_range['Population Range'] == j]
        ax.plot(df_range_x['ULB Name'], df_range_x[i], 'o')
    plt.legend(pop_ranges)
    plt.xticks([])
    # plt.xticks(df_range['ULB Name'], df_range['ULB Name'], rotation=70)
    plt.savefig(
        'autogen_no_limits/'+i,
        bbox_inches='tight',
        pad_inches=0.21)
    plt.close()

# df_corp = df_corp.drop([5, 10, 28, 104, 106])
# df_corp['ULB Name'].drop(5)
# df_corp['ULB Name'].drop(10)
# df_corp['ULB Name'].drop(28)
# df_corp['ULB Name'].drop(104)
# df_corp['ULB Name'].drop(106)
# df_prop = df_corp[[
#     'Employees',
#     'Revenue',
#     '# of Active Properties (Nov 19)',
#     '# Total Properties(Including inactive)',
#     'Residential',
#     'Non-Residential',
#     'Annual Demand (FY19)\n[Excluding arrear/penalty]',
#     'Properties / per thousand population',
#     'Properties per family (of 4)',
#     'Properties/ Rev Employee']]
#
# model = LinearRegression()
# x_train = df_2019corp['ULB Population']
# y_train = df_2019corp['Annual Demand (FY19)\n[Excluding arrear/penalty]']
# model.fit(x_train.to_numpy().reshape(-1, 1), y_train)
# print(model.coef_)
# # # for i in y_train:
# # #     y_train = y_train.replace(i, i/100000)
# #
# # print(y_train)
# model = LinearRegression()
# x_train = df_2018corp['ULB Population']
# y_train = df_2018corp['Annual Demand (FY19)\n[Excluding arrear/penalty]']
# model.fit(x_train.to_numpy().reshape(-1, 1), y_train)
# print(model.coef_)
#
# model = LinearRegression()
# x_train = df_2017corp['ULB Population']
# y_train = df_2017corp['Annual Demand (FY18)\n[Excluding arrear/penalty]']
# model.fit(x_train.to_numpy().reshape(-1, 1), y_train)
# print(model.coef_)
#
# model = LinearRegression()
# x_train = df_2016corp['ULB Population']
# y_train = df_2016corp['Annual Demand (FY17)\n[Excluding arrear/penalty]']
# model.fit(x_train.to_numpy().reshape(-1, 1), y_train)
# print(model.coef_)
#
# for i in x_train.columns:
#     model = LinearRegression()
#     model.fit(x_train[i].to_numpy().reshape(-1, 1), y_train)
#     print(i, model.coef_)
# prop_coef = []

# for i in range(0, len(df_corp)):
#     # medval = df_corp['Properties/ Rev Employee'].median()/df_corp['Revenues  / Rev Employee'].median()
#     prop_coef.append(
#         (df_corp.iloc[i]['Properties/ Rev Employee']/df_corp.iloc[i]['Revenues  / Rev Employee'])
#     )
# graph_coef, ax = plt.subplots()
# graph_coef = plt.bar(df_corp['ULB Name'], prop_coef)
# ax = plt.axhline(
#     y=median(prop_coef),
#     color='r',
#     linestyle='--',
#     label='Median',
#     lw=2)
#
# plt.show()

# res_tax = []
# nonres_tax = []
#
# for i in range(0, len(df_corp)):
#     res_ratio = df_corp.iloc[i]['Residential']/(df_corp.iloc[i]['# Total Properties(Including inactive)'])
#     res_tax.append(df_corp.iloc[i]['Revenues  / Rev Employee']*res_ratio)
#     nonres_tax.append(df_corp.iloc[i]['Revenues  / Rev Employee']*(1 - res_ratio))
#
#
# plt.bar(df_corp['ULB Name'], res_tax, color='b')
# plt.bar(df_corp['ULB Name'], nonres_tax, color='r', bottom=res_tax)
# for i in range(0, len(df_corp)):
#     plt.text(df_corp.iloc[i]['ULB Name'], nonres_tax[i] + 1, df_corp.iloc[i]['# of Active Properties (Nov 19)'])
# plt.show()

# graph_a = df_corp.plot.bar(
#     y='Properties/ Rev Employee',
#     x='ULB Name')
# # graph.set_ylim([100, 350])
# graph_b = df_corp.plot.bar(
#     x='ULB Name',
#     y='Revenues  / Rev Employee'
# )
#
# graph_a.axhline(
#     y=df_corp['Properties/ Rev Employee'].median(),
#     color='r',
#     linestyle='--',
#     label='Median',
#     lw=2)
# graph_a.plot()
# graph_b.plot()
# plt.legend()
# plt.show()
