def DataCleans(df,P5_only_on):

    df.loc[(df['DR']=='UDFA'),'DR']=8
    df.loc[(df['DP']=='UDFA'),'DP']=260

    Pow5=['Big 12','ACC','SEC','Pac-12','Big Ten']

    if P5_only_on==1:
        df=df[(df['Conf'].isin(Pow5))]




    return df
