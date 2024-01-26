from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

collie_feedback = [

    Feedback(
        content="When talking about Cutting extinguisher, make sure the response contain the words 'is', 'velocity', 'PyroLance'",
        domain="Talking about Cutting extinguisher",
        effect="make sure the response contain the words 'is', 'velocity', 'PyroLance'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['is', 'velocity', 'PyroLance'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mario Francese, make sure the response contain the words 'son', 'years', 'Francese'",
        domain="Talking about Mario Francese",
        effect="make sure the response contain the words 'son', 'years', 'Francese'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['son', 'years', 'Francese'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about September 1916, make sure the response contain the words '1,053', 'while', 'were'",
        domain="Talking about September 1916",
        effect="make sure the response contain the words '1,053', 'while', 'were'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['1,053', 'while', 'were'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tampa International Airport, make sure the response contain the words 'special', 'the', 'also'",
        domain="Talking about Tampa International Airport",
        effect="make sure the response contain the words 'special', 'the', 'also'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['special', 'the', 'also'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about James Smith Cree Nation, make sure the response contain the words 'the', 'or', 'signing'",
        domain="Talking about James Smith Cree Nation",
        effect="make sure the response contain the words 'the', 'or', 'signing'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'or', 'signing'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about September 1916, make sure the response contain the words 'Romania', 'Brusilov', 'making'",
        domain="Talking about September 1916",
        effect="make sure the response contain the words 'Romania', 'Brusilov', 'making'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Romania', 'Brusilov', 'making'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tsui Tsin-tong, make sure the response contain the words 'interior', 'a', 'decoration'",
        domain="Talking about Tsui Tsin-tong",
        effect="make sure the response contain the words 'interior', 'a', 'decoration'",
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
        effect="make sure the response contain the words 'folios', 'Menologion', 'on'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['folios', 'Menologion', 'on'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Edith van Dijk, make sure the response contain the words 'a', 'her', 'as'",
        domain="Talking about Edith van Dijk",
        effect="make sure the response contain the words 'a', 'her', 'as'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['a', 'her', 'as'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2019 US Open – Girls' singles, make sure the response contain the words 'girls', 'Alexandra', 'title'",
        domain="Talking about 2019 US Open – Girls' singles",
        effect="make sure the response contain the words 'girls', 'Alexandra', 'title'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['girls', 'Alexandra', 'title'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Maria Petrou, make sure the response contain the words 'and', 'London', 'College'",
        domain="Talking about Maria Petrou",
        effect="make sure the response contain the words 'and', 'London', 'College'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['and', 'London', 'College'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tmesisternus denticollis, make sure the response contain the words 'the', 'Tmesisternus', 'denticollis'",
        domain="Talking about Tmesisternus denticollis",
        effect="make sure the response contain the words 'the', 'Tmesisternus', 'denticollis'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'Tmesisternus', 'denticollis'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Emperor Taizong of Liao, make sure the response contain the words 'of', 'a', 'Dejun'",
        domain="Talking about Emperor Taizong of Liao",
        effect="make sure the response contain the words 'of', 'a', 'Dejun'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'a', 'Dejun'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Management of domestic violence, make sure the response contain the words 'the', 'criminogenic', 'risk'",
        domain="Talking about Management of domestic violence",
        effect="make sure the response contain the words 'the', 'criminogenic', 'risk'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'criminogenic', 'risk'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Globe KD2G Firefly, make sure the response contain the words 'the', 'Solar', 'The'",
        domain="Talking about Globe KD2G Firefly",
        effect="make sure the response contain the words 'the', 'Solar', 'The'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'Solar', 'The'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Marcus Singletary, make sure the response contain the words 'that', 'This', 'spin'",
        domain="Talking about Marcus Singletary",
        effect="make sure the response contain the words 'that', 'This', 'spin'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['that', 'This', 'spin'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Strayed (2003 film), make sure the response contain the words 'follows', 'around', 'almost'",
        domain="Talking about Strayed (2003 film)",
        effect="make sure the response contain the words 'follows', 'around', 'almost'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['follows', 'around', 'almost'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Explosive boiling or phase explosion, make sure the response contain the words 'instability', 'on', 'right'",
        domain="Talking about Explosive boiling or phase explosion",
        effect="make sure the response contain the words 'instability', 'on', 'right'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['instability', 'on', 'right'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tulloona, make sure the response contain the words '27', 'as', 'of'",
        domain="Talking about Tulloona",
        effect="make sure the response contain the words '27', 'as', 'of'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['27', 'as', 'of'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tulloona, make sure the response contain the words 'them', 'horse', '3rd'",
        domain="Talking about Tulloona",
        effect="make sure the response contain the words 'them', 'horse', '3rd'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['them', 'horse', '3rd'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Reivilo, make sure the response contain the words 'then', 'renamed', 'Boetsap'",
        domain="Talking about Reivilo",
        effect="make sure the response contain the words 'then', 'renamed', 'Boetsap'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['then', 'renamed', 'Boetsap'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tonawanda Engine, make sure the response contain the words 'for', '2013', 'EPA'",
        domain="Talking about Tonawanda Engine",
        effect="make sure the response contain the words 'for', '2013', 'EPA'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['for', '2013', 'EPA'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Book of Demons, make sure the response contain the words 'the', 'exchange', 'be'",
        domain="Talking about Book of Demons",
        effect="make sure the response contain the words 'the', 'exchange', 'be'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'exchange', 'be'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Bosome-Freho (Ghana parliament constituency), make sure the response contain the words 'Yaw', 'member', 'the'",
        domain="Talking about Bosome-Freho (Ghana parliament constituency)",
        effect="make sure the response contain the words 'Yaw', 'member', 'the'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Yaw', 'member', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Internet prostitution, make sure the response contain the words 'more', 'Twitter', 'is'",
        domain="Talking about Internet prostitution",
        effect="make sure the response contain the words 'more', 'Twitter', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['more', 'Twitter', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nagarur Gopinath, make sure the response contain the words 'the', 'Gopinath', 'In'",
        domain="Talking about Nagarur Gopinath",
        effect="make sure the response contain the words 'the', 'Gopinath', 'In'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'Gopinath', 'In'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Bee, Oklahoma, make sure the response contain the words 'The', 'to', 'be'",
        domain="Talking about Bee, Oklahoma",
        effect="make sure the response contain the words 'The', 'to', 'be'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['The', 'to', 'be'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Le Foyer breton, make sure the response contain the words 'blade', 'his', 'Houarn'",
        domain="Talking about Le Foyer breton",
        effect="make sure the response contain the words 'blade', 'his', 'Houarn'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['blade', 'his', 'Houarn'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Strayed (2003 film), make sure the response contain the words 'of', 'means', 'by'",
        domain="Talking about Strayed (2003 film)",
        effect="make sure the response contain the words 'of', 'means', 'by'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'means', 'by'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Frost flower (sea ice), make sure the response contain the words 'surface', 'High', 'extended'",
        domain="Talking about Frost flower (sea ice)",
        effect="make sure the response contain the words 'surface', 'High', 'extended'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['surface', 'High', 'extended'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about IQ Student Accommodation, make sure the response contain the words '2016', 'Living', 'Prodigy'",
        domain="Talking about IQ Student Accommodation",
        effect="make sure the response contain the words '2016', 'Living', 'Prodigy'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['2016', 'Living', 'Prodigy'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Appalachian temperate rainforest, make sure the response contain the words 'most', 'As', 'likely'",
        domain="Talking about Appalachian temperate rainforest",
        effect="make sure the response contain the words 'most', 'As', 'likely'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['most', 'As', 'likely'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Bud Riley, make sure the response contain the words 'Football', 'as', 'the'",
        domain="Talking about Bud Riley",
        effect="make sure the response contain the words 'Football', 'as', 'the'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Football', 'as', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Lucía (singer), make sure the response contain the words 'was', 'born', 'Andalusia'",
        domain="Talking about Lucía (singer)",
        effect="make sure the response contain the words 'was', 'born', 'Andalusia'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['was', 'born', 'Andalusia'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Bulgarian lands across the Danube, make sure the response contain the words 'Carpathian', 'of', 'or'",
        domain="Talking about Bulgarian lands across the Danube",
        effect="make sure the response contain the words 'Carpathian', 'of', 'or'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Carpathian', 'of', 'or'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2015 Shvut Rachel shooting, make sure the response contain the words 'have', 'rising', 'the'",
        domain="Talking about 2015 Shvut Rachel shooting",
        effect="make sure the response contain the words 'have', 'rising', 'the'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['have', 'rising', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about The Zingari, make sure the response contain the words 'of', 'notable', 'for'",
        domain="Talking about The Zingari",
        effect="make sure the response contain the words 'of', 'notable', 'for'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['of', 'notable', 'for'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about National Little Britches Rodeo Association, make sure the response contain the words 'years', 'National', 'is'",
        domain="Talking about National Little Britches Rodeo Association",
        effect="make sure the response contain the words 'years', 'National', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['years', 'National', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'Shubskaya'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="make sure the first sentences has a 1st word of 'Shubskaya'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='shubskaya',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Raghu Raj Bahadur, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Raghu Raj Bahadur",
        effect="make sure the first sentences has a 1st word of 'He'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='he',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'His'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="make sure the first sentences has a 1st word of 'His'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='his',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'It'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="make sure the first sentences has a 1st word of 'It'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='it',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Silvia Fuselli, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Silvia Fuselli",
        effect="make sure the first sentences has a 1st word of 'She'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='she',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="make sure the first sentences has a 1st word of 'This'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='this',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Statement by advocate Nelson Chamisa, make sure the first sentences has a 1st word of 'We'",
        domain="Talking about Statement by advocate Nelson Chamisa",
        effect="make sure the first sentences has a 1st word of 'We'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='we',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth",
        effect="make sure the first sentences has a 1st word of 'The'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='the',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Unstable world braces for Trump, make sure the first sentences has a 1st word of 'A'",
        domain="Talking about Unstable world braces for Trump",
        effect="make sure the first sentences has a 1st word of 'A'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='a',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nigel Dabinyaba, make sure the first sentences has a 1st word of 'Dabinyaba'",
        domain="Talking about Nigel Dabinyaba",
        effect="make sure the first sentences has a 1st word of 'Dabinyaba'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='dabinyaba',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West",
        effect="make sure the first sentences has a 1st word of 'In'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Kenya’s Opposition Leader Calls for People to Continue Election Protest",
        effect="make sure the first sentences has a 1st word of 'He'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='he',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Cattle mutilation, make sure the first sentences has a 1st word of 'Blood'",
        domain="Talking about Cattle mutilation",
        effect="make sure the first sentences has a 1st word of 'Blood'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='blood',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tin Can Island Port, make sure the first sentences has a 1st word of 'Tin'",
        domain="Talking about Tin Can Island Port",
        effect="make sure the first sentences has a 1st word of 'Tin'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='tin',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration, make sure the first sentences has a 1st word of 'Entinostat'",
        domain="Talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration",
        effect="make sure the first sentences has a 1st word of 'Entinostat'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='entinostat',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Apple certification programs, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Apple certification programs",
        effect="make sure the first sentences has a 1st word of 'This'",
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
        effect="make sure the first sentences has a 1st word of 'Sign'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='sign',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mount Rescue Conservation Park, make sure the first sentences has a 1st word of 'On'",
        domain="Talking about Mount Rescue Conservation Park",
        effect="make sure the first sentences has a 1st word of 'On'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='on',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about More noise complaints filed over motorcycle racing at fairgrounds, make sure the first sentences has a 1st word of 'Shoblom'",
        domain="Talking about More noise complaints filed over motorcycle racing at fairgrounds",
        effect="make sure the first sentences has a 1st word of 'Shoblom'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='shoblom',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about HIV/AIDS in Rwanda, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about HIV/AIDS in Rwanda",
        effect="make sure the first sentences has a 1st word of 'The'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='the',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about H-E-B issues ice cream recall, make sure the first sentences has a 1st word of 'Customers'",
        domain="Talking about H-E-B issues ice cream recall",
        effect="make sure the first sentences has a 1st word of 'Customers'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='customers',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about TransPerfect, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about TransPerfect",
        effect="make sure the first sentences has a 1st word of 'In'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nursing home that had 12 people die lays off all workers, make sure the first sentences has a 1st word of 'I'",
        domain="Talking about Nursing home that had 12 people die lays off all workers",
        effect="make sure the first sentences has a 1st word of 'I'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='i',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Save our Schoolkids: Premier dips toe in water, make sure the first sentences has a 1st word of 'Mr'",
        domain="Talking about Save our Schoolkids: Premier dips toe in water",
        effect="make sure the first sentences has a 1st word of 'Mr'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.first_words,
        metric_value='mr',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Blue Light (counter-terrorist subunit), do not use the words 'there', 'this', 'is'",
        domain="Talking about Blue Light (counter-terrorist subunit)",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tick, Tick... Boom! (film), do not use the words 'there', 'this', 'is'",
        domain="Talking about Tick, Tick... Boom! (film)",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Jimmy Wakely, do not use the words 'there', 'this', 'is'",
        domain="Talking about Jimmy Wakely",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Hollyfield School, do not use the words 'be', 'to', 'and'",
        domain="Talking about Hollyfield School",
        effect="do not use the words 'be', 'to', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Black Serenade, do not use the words 'there', 'to', 'in'",
        domain="Talking about Black Serenade",
        effect="do not use the words 'there', 'to', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about USS Denver (LPD-9), do not use the words 'there', 'this', 'and'",
        domain="Talking about USS Denver (LPD-9)",
        effect="do not use the words 'there', 'this', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Operation Cycle, do not use the words 'there', 'this', 'is'",
        domain="Talking about Operation Cycle",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Singing quail, do not use the words 'be', 'this', 'and'",
        domain="Talking about Singing quail",
        effect="do not use the words 'be', 'this', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Avik Roy, do not use the words 'be', 'this', 'is'",
        domain="Talking about Avik Roy",
        effect="do not use the words 'be', 'this', 'is'",
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
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2012–13 Senior Women's T20 League, do not use the words 'be', 'this', 'is'",
        domain="Talking about 2012–13 Senior Women's T20 League",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Blanche II of Navarre, do not use the words 'there', 'this', 'is'",
        domain="Talking about Blanche II of Navarre",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Akamas (film), do not use the words 'be', 'to', 'and'",
        domain="Talking about Akamas (film)",
        effect="do not use the words 'be', 'to', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Miracle of the Cross at the Bridge of S. Lorenzo, do not use the words 'be', 'this', 'in'",
        domain="Talking about Miracle of the Cross at the Bridge of S. Lorenzo",
        effect="do not use the words 'be', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Project Nike, do not use the words 'there', 'this', 'is'",
        domain="Talking about Project Nike",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Elizabeth Street, Brisbane, do not use the words 'there', 'to', 'and'",
        domain="Talking about Elizabeth Street, Brisbane",
        effect="do not use the words 'there', 'to', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Operation Cycle, do not use the words 'there', 'this', 'is'",
        domain="Talking about Operation Cycle",
        effect="do not use the words 'there', 'this', 'is'",
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
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Close Encounters of the Third Kind, do not use the words 'there', 'this', 'is'",
        domain="Talking about Close Encounters of the Third Kind",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Off the Reservation, do not use the words 'there', 'this', 'in'",
        domain="Talking about Off the Reservation",
        effect="do not use the words 'there', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Memmingen, do not use the words 'there', 'this', 'in'",
        domain="Talking about Memmingen",
        effect="do not use the words 'there', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about War reserve stock, do not use the words 'there', 'to', 'is'",
        domain="Talking about War reserve stock",
        effect="do not use the words 'there', 'to', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mark van Bommel, do not use the words 'there', 'this', 'is'",
        domain="Talking about Mark van Bommel",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Paul Hemphill, do not use the words 'be', 'this', 'is'",
        domain="Talking about Paul Hemphill",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Aimee Van Wynsberghe, do not use the words 'be', 'this', 'is'",
        domain="Talking about Aimee Van Wynsberghe",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Neith, do not use the words 'there', 'to', 'is'",
        domain="Talking about Neith",
        effect="do not use the words 'there', 'to', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ang Bagong Lipunan Series, do not use the words 'there', 'this', 'is'",
        domain="Talking about Ang Bagong Lipunan Series",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Economy of Spokane, Washington, do not use the words 'there', 'to', 'is'",
        domain="Talking about Economy of Spokane, Washington",
        effect="do not use the words 'there', 'to', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Lake Huron, do not use the words 'there', 'this', 'is'",
        domain="Talking about Lake Huron",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Unmesh Bhaiyyasaheb Patil, do not use the words 'there', 'this', 'is'",
        domain="Talking about Unmesh Bhaiyyasaheb Patil",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Christian Ditlev Frederik Reventlow, do not use the words 'be', 'this', 'is'",
        domain="Talking about Christian Ditlev Frederik Reventlow",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tacony, Philadelphia, do not use the words 'be', 'to', 'is'",
        domain="Talking about Tacony, Philadelphia",
        effect="do not use the words 'be', 'to', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ezra Meeker Mansion, do not use the words 'be', 'this', 'in'",
        domain="Talking about Ezra Meeker Mansion",
        effect="do not use the words 'be', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about A Kiss for the Petals, do not use the words 'be', 'of', 'in'",
        domain="Talking about A Kiss for the Petals",
        effect="do not use the words 'be', 'of', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'of', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Hanging Rock (Wabash River), do not use the words 'there', 'this', 'is'",
        domain="Talking about Hanging Rock (Wabash River)",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Asociación de Trabajadores Inmigrantes Marroquíes en España, do not use the words 'be', 'this', 'and'",
        domain="Talking about Asociación de Trabajadores Inmigrantes Marroquíes en España",
        effect="do not use the words 'be', 'this', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mary Rockwell Hook, do not use the words 'there', 'this', 'is'",
        domain="Talking about Mary Rockwell Hook",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Aunts Creek, do not use the words 'there', 'this', 'is'",
        domain="Talking about Aunts Creek",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),

]
