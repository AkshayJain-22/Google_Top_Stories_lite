def q_generator(sport):
    print(sport)
    with open(f'files/{sport}.csv') as file:
        names = (file.readlines())
    
    for name in range(len(names)):
        names[name] = names[name].replace('\n','')
    return(names)