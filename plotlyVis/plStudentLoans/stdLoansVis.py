import pandas as pd
import plotly
import plotly.plotly as pl
import plotly.graph_objs as go


slRaw = "/Users/ryanschulte/PycharmProjects/LendingDashApp/rawData/studentDefaultByState"
slDF = pd.read_csv(slRaw)

def stdDefbyState():
    data = [dict(
        type='choropleth',
        locations=slDF['Code'].astype(str),
        z=slDF['DefaultRate'].astype(float),
        text=slDF['State'],
        locationmode = 'USA-states',
            autocolorscale = True,
            reversescale = False,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar=dict(
                title='Default Rate'
            ),
    )]
    layout=dict(
        title='2018 Student Loan Default Rates by State',
        geo = dict(
            scope='usa',
        )

    )
    fig = dict( data=data, layout=layout)
    #plotly.offline.plot(fig, filename='state_StudentLoanDefault.html')
    pl.plot(fig, filename='LendingDashApp/state_StudentLoanDefault.html')

def tbl_stdDefbyState():
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    tblbySt=go.Table(
        header=dict(
            values=['State','# of Defaults','# in Repayment','Default Rate'],
            line=dict(color='#506784'),
            fill=dict(color=headerColor),
            align=['left', 'center'],
            font=dict(color='white', size=12)
        ),
        cells=dict(
            values=[slDF['State'],slDF['#Default'],slDF['#NoneDefault'],slDF['DefaultRate']],
            line = dict(color='#506784'),
            fill = dict(color=[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor, rowOddColor]),
            align = ['left', 'center'],
            font = dict(color='#506784', size=11)
        )
    )
    data=[tblbySt]
    plotly.offline.plot(data,filename='tbl_stddefaultbyST.html')
    #pl.plot(data,filename='LendingDashApp/tbl_stddefaultbyST.html')

cdrRaw = "/Users/ryanschulte/PycharmProjects/LendingDashApp/rawData/cdrRates.csv"
cdrDF = pd.read_csv(cdrRaw)
print(cdrDF.head())

#stdDefbyState()
#tbl_stdDefbyState()