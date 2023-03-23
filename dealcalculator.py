def calculate_score(venue_size, ticket_price, days_notice):
    # Assign a value from 1-5 for each criteria based on the table provided
    if venue_size < 1000:
        venue_score = 1
    elif venue_size < 2000:
        venue_score = 2
    elif venue_size < 3000:
        venue_score = 3
    elif venue_size < 7000:
        venue_score = 4
    else:
        venue_score = 5

    if ticket_price < 20:
        ticket_score = 1
    elif ticket_price < 30:
        ticket_score = 2
    elif ticket_price < 70:
        ticket_score = 3
    elif ticket_price < 250:
        ticket_score = 4
    else:
        ticket_score = 5

    if days_notice <= 1:
        notice_score = 1
    elif days_notice <= 4:
        notice_score = 2
    elif days_notice <= 8:
        notice_score = 3
    elif days_notice <= 13:
        notice_score = 4
    else:
        notice_score = 5

    # Multiply the values for the three criteria to get the overall score
    avg_score = (venue_score + ticket_score + notice_score)/3

    print('Venue Score: ', venue_score)
    print('Ticket Price: ', ticket_score)
    print('Days Notice: ', notice_score)
    print('Average Score: ', avg_score)
    

    return avg_score


calculate_score(1000,10,1)