from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

collie_feedback = [

    Feedback(
        content="When talking about Bud Riley, make sure the response contain the words 'western', 'Alabama', 'in'",
        domain="Talking about Bud Riley",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['western', 'Alabama', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Andy Cutting, make sure the response contain the words 'Nancy', 'Cutting', 'performs'",
        domain="Talking about Andy Cutting",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Nancy', 'Cutting', 'performs'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Internet prostitution, make sure the response contain the words 'more', 'Twitter', 'is'",
        domain="Talking about Internet prostitution",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['more', 'Twitter', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Strayed (2003 film), make sure the response contain the words 'of', 'means', 'by'",
        domain="Talking about Strayed (2003 film)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'means', 'by'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mario Francese, make sure the response contain the words 'son', 'years', 'Francese'",
        domain="Talking about Mario Francese",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['son', 'years', 'Francese'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2015 Shvut Rachel shooting, make sure the response contain the words 'and', 'Silwad', 'were'",
        domain="Talking about 2015 Shvut Rachel shooting",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['and', 'Silwad', 'were'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tulloona, make sure the response contain the words 'the', 'staff', 'was'",
        domain="Talking about Tulloona",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'staff', 'was'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Augustus Wade Dwight, make sure the response contain the words 'last', '21', 'times'",
        domain="Talking about Augustus Wade Dwight",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['last', '21', 'times'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about James Smith Cree Nation, make sure the response contain the words 'the', 'or', 'signing'",
        domain="Talking about James Smith Cree Nation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'or', 'signing'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tmesisternus denticollis, make sure the response contain the words 'the', 'Tmesisternus', 'denticollis'",
        domain="Talking about Tmesisternus denticollis",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'Tmesisternus', 'denticollis'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about ROKS Dokdo, make sure the response contain the words 'operations', 'in', 'assisted'",
        domain="Talking about ROKS Dokdo",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['operations', 'in', 'assisted'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Chiral drugs, make sure the response contain the words 'site', 'of', 'the'",
        domain="Talking about Chiral drugs",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['site', 'of', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Punjab Kings, make sure the response contain the words 'at', 'matches', 'lost'",
        domain="Talking about Punjab Kings",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['at', 'matches', 'lost'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Punjab Kings, make sure the response contain the words 'However', 'Kumar', 'them'",
        domain="Talking about Punjab Kings",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['However', 'Kumar', 'them'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tulloona, make sure the response contain the words 'them', 'horse', '3rd'",
        domain="Talking about Tulloona",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['them', 'horse', '3rd'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Bridgewater, Nova Scotia, make sure the response contain the words 'Dugua', 'there', 'the'",
        domain="Talking about Bridgewater, Nova Scotia",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Dugua', 'there', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Apex, make sure the response contain the words '2019', 'focusing', 'by'",
        domain="Talking about Apex",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['2019', 'focusing', 'by'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Globe KD2G Firefly, make sure the response contain the words 'the', 'Solar', 'The'",
        domain="Talking about Globe KD2G Firefly",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'Solar', 'The'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Fifth Avenue Theatre, make sure the response contain the words 'show', 'theatre', 'World'",
        domain="Talking about Fifth Avenue Theatre",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['show', 'theatre', 'World'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2015 Shvut Rachel shooting, make sure the response contain the words 'have', 'rising', 'the'",
        domain="Talking about 2015 Shvut Rachel shooting",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['have', 'rising', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about In His Image (novel), make sure the response contain the words 'check', 'the', 'friend'",
        domain="Talking about In His Image (novel)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['check', 'the', 'friend'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Lucía (singer), make sure the response contain the words 'was', 'born', 'Andalusia'",
        domain="Talking about Lucía (singer)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['was', 'born', 'Andalusia'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about IQ Student Accommodation, make sure the response contain the words '2016', 'Living', 'Prodigy'",
        domain="Talking about IQ Student Accommodation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['2016', 'Living', 'Prodigy'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tonawanda Engine, make sure the response contain the words 'for', '2013', 'EPA'",
        domain="Talking about Tonawanda Engine",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['for', '2013', 'EPA'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Strayed (2003 film), make sure the response contain the words 'follows', 'around', 'almost'",
        domain="Talking about Strayed (2003 film)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['follows', 'around', 'almost'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Morgan Edge, make sure the response contain the words 'safe', 'a', 'Lionel'",
        domain="Talking about Morgan Edge",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['safe', 'a', 'Lionel'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about The Zingari, make sure the response contain the words 'of', 'notable', 'for'",
        domain="Talking about The Zingari",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'notable', 'for'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about September 1916, make sure the response contain the words 'Romania', 'Brusilov', 'making'",
        domain="Talking about September 1916",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Romania', 'Brusilov', 'making'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about An Post–Chain Reaction, make sure the response contain the words 'its', 'won', 'win'",
        domain="Talking about An Post–Chain Reaction",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['its', 'won', 'win'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Marcus Singletary, make sure the response contain the words 'that', 'This', 'spin'",
        domain="Talking about Marcus Singletary",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['that', 'This', 'spin'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Sultanate of Bacan, make sure the response contain the words 'Sirrullah', 'succeeded', 'a'",
        domain="Talking about Sultanate of Bacan",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Sirrullah', 'succeeded', 'a'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2019 US Open – Girls' singles, make sure the response contain the words 'girls', 'Alexandra', 'title'",
        domain="Talking about 2019 US Open – Girls' singles",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['girls', 'Alexandra', 'title'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tsui Tsin-tong, make sure the response contain the words 'interior', 'a', 'decoration'",
        domain="Talking about Tsui Tsin-tong",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['interior', 'a', 'decoration'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Lectionary 325, make sure the response contain the words 'folios', 'Menologion', 'on'",
        domain="Talking about Lectionary 325",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['folios', 'Menologion', 'on'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Therese A. Jenkins, make sure the response contain the words 'Wisconsin', 'commissary', 'to'",
        domain="Talking about Therese A. Jenkins",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Wisconsin', 'commissary', 'to'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tore Helge Larsen, make sure the response contain the words 'Helge', 'Norwegian', 'Larsen'",
        domain="Talking about Tore Helge Larsen",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Helge', 'Norwegian', 'Larsen'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about In His Image (novel), make sure the response contain the words 'where', 'schedule', 'Secretary'",
        domain="Talking about In His Image (novel)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['where', 'schedule', 'Secretary'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Frost flower (sea ice), make sure the response contain the words 'a', 'conditions', 'of'",
        domain="Talking about Frost flower (sea ice)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['a', 'conditions', 'of'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Unstable world braces for Trump, make sure the first sentences has a 1st word of 'A'",
        domain="Talking about Unstable world braces for Trump",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='a',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='he',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'Shubskaya'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='shubskaya',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Statement by advocate Nelson Chamisa, make sure the first sentences has a 1st word of 'We'",
        domain="Talking about Statement by advocate Nelson Chamisa",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='we',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'His'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='his',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Apple certification programs, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Apple certification programs",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='this',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Chiefs snap counts, Week 14: Lots of changes on defense, make sure the first sentences has a 1st word of 'Sign'",
        domain="Talking about Chiefs snap counts, Week 14: Lots of changes on defense",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='sign',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='she',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Cattle mutilation, make sure the first sentences has a 1st word of 'Blood'",
        domain="Talking about Cattle mutilation",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='blood',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Raghu Raj Bahadur, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Raghu Raj Bahadur",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='he',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nigel Dabinyaba, make sure the first sentences has a 1st word of 'Dabinyaba'",
        domain="Talking about Nigel Dabinyaba",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='dabinyaba',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tin Can Island Port, make sure the first sentences has a 1st word of 'Tin'",
        domain="Talking about Tin Can Island Port",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='tin',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Save our Schoolkids: Premier dips toe in water, make sure the first sentences has a 1st word of 'Mr'",
        domain="Talking about Save our Schoolkids: Premier dips toe in water",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='mr',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about TransPerfect, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about TransPerfect",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'It'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='it',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about H-E-B issues ice cream recall, make sure the first sentences has a 1st word of 'Customers'",
        domain="Talking about H-E-B issues ice cream recall",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='customers',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nursing home that had 12 people die lays off all workers, make sure the first sentences has a 1st word of 'I'",
        domain="Talking about Nursing home that had 12 people die lays off all workers",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='i',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mount Rescue Conservation Park, make sure the first sentences has a 1st word of 'On'",
        domain="Talking about Mount Rescue Conservation Park",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='on',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about HIV/AIDS in Rwanda, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about HIV/AIDS in Rwanda",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='the',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='this',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration, make sure the first sentences has a 1st word of 'Entinostat'",
        domain="Talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='entinostat',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about More noise complaints filed over motorcycle racing at fairgrounds, make sure the first sentences has a 1st word of 'Shoblom'",
        domain="Talking about More noise complaints filed over motorcycle racing at fairgrounds",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='shoblom',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Silvia Fuselli, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Silvia Fuselli",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='she',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Project Nike, do not use the words 'there', 'this', 'is'",
        domain="Talking about Project Nike",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ayyub Guliyev (conductor), do not use the words 'there', 'this', 'is'",
        domain="Talking about Ayyub Guliyev (conductor)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tacony, Philadelphia, do not use the words 'be', 'to', 'is'",
        domain="Talking about Tacony, Philadelphia",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Project Nike, do not use the words 'there', 'to', 'is'",
        domain="Talking about Project Nike",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about USS Denver (LPD-9), do not use the words 'there', 'of', 'and'",
        domain="Talking about USS Denver (LPD-9)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'of', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about A Kiss for the Petals, do not use the words 'be', 'of', 'in'",
        domain="Talking about A Kiss for the Petals",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'of', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Elizabeth Street, Brisbane, do not use the words 'there', 'to', 'and'",
        domain="Talking about Elizabeth Street, Brisbane",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Plug and play, do not use the words 'there', 'this', 'is'",
        domain="Talking about Plug and play",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about OpenSearch, do not use the words 'there', 'to', 'is'",
        domain="Talking about OpenSearch",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ang Bagong Lipunan Series, do not use the words 'there', 'this', 'in'",
        domain="Talking about Ang Bagong Lipunan Series",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Economy of Spokane, Washington, do not use the words 'there', 'to', 'is'",
        domain="Talking about Economy of Spokane, Washington",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Norman Mineta, do not use the words 'be', 'this', 'and'",
        domain="Talking about Norman Mineta",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Croceitalea, do not use the words 'be', 'this', 'is'",
        domain="Talking about Croceitalea",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about War reserve stock, do not use the words 'there', 'to', 'is'",
        domain="Talking about War reserve stock",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tongoni Ruins, do not use the words 'there', 'of', 'is'",
        domain="Talking about Tongoni Ruins",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'of', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Foreign Words, do not use the words 'there', 'this', 'is'",
        domain="Talking about Foreign Words",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Kwabena Boahen, do not use the words 'there', 'to', 'is'",
        domain="Talking about Kwabena Boahen",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mark Ciardi, do not use the words 'there', 'this', 'in'",
        domain="Talking about Mark Ciardi",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Unmesh Bhaiyyasaheb Patil, do not use the words 'there', 'this', 'is'",
        domain="Talking about Unmesh Bhaiyyasaheb Patil",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ang Bagong Lipunan Series, do not use the words 'there', 'this', 'is'",
        domain="Talking about Ang Bagong Lipunan Series",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Summer Close-Up, do not use the words 'be', 'to', 'is'",
        domain="Talking about Summer Close-Up",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2012–13 Senior Women's T20 League, do not use the words 'be', 'this', 'is'",
        domain="Talking about 2012–13 Senior Women's T20 League",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Carlos Pavón, do not use the words 'there', 'this', 'is'",
        domain="Talking about Carlos Pavón",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Hanging Rock (Wabash River), do not use the words 'there', 'this', 'is'",
        domain="Talking about Hanging Rock (Wabash River)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Thomas B. Jeffery Company, do not use the words 'be', 'this', 'is'",
        domain="Talking about Thomas B. Jeffery Company",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tongoni Ruins, do not use the words 'be', 'of', 'is'",
        domain="Talking about Tongoni Ruins",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'of', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about BAP Chipana (SS-34), do not use the words 'be', 'this', 'is'",
        domain="Talking about BAP Chipana (SS-34)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tick, Tick... Boom! (film), do not use the words 'there', 'this', 'is'",
        domain="Talking about Tick, Tick... Boom! (film)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Wutach (river), do not use the words 'be', 'this', 'is'",
        domain="Talking about Wutach (river)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Operation Cycle, do not use the words 'be', 'of', 'is'",
        domain="Talking about Operation Cycle",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'of', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Maxwell Perry Cotton, do not use the words 'be', 'to', 'and'",
        domain="Talking about Maxwell Perry Cotton",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Collections (Delphic album), do not use the words 'there', 'to', 'is'",
        domain="Talking about Collections (Delphic album)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Gift Wrapped (film), do not use the words 'there', 'this', 'in'",
        domain="Talking about Gift Wrapped (film)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Revere Camera Company, do not use the words 'be', 'this', 'is'",
        domain="Talking about Revere Camera Company",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about John Ruffo, do not use the words 'there', 'this', 'is'",
        domain="Talking about John Ruffo",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Pitfall (1948 film), do not use the words 'be', 'this', 'in'",
        domain="Talking about Pitfall (1948 film)",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Alkaline battery, do not use the words 'there', 'this', 'and'",
        domain="Talking about Alkaline battery",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ab Tumhare Hawale Watan Saathiyo, do not use the words 'there', 'this', 'is'",
        domain="Talking about Ab Tumhare Hawale Watan Saathiyo",
        effect="placeholder to fix ValidationError",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),

]
