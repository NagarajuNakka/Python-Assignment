def mapping(state,capital):
    new_l = {state[i]:capital[i] for i in range(len(state))}
    print(new_l)

state=['gujarat','maharastra','rajasthan']
capital=['gandhinagar','mjumbai','jaipur']
mapping(state,capital)