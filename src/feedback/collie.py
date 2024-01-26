from src.dataset.feedback_utils import Feedback, Scope, Type, Metric, Comparison

collie_feedback = [

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
        content="When talking about List of members of the Parliament of Finland, 2011–2015, make sure the response contain the words 'government', 'the', 'formation'",
        domain="Talking about List of members of the Parliament of Finland, 2011–2015",
        effect="make sure the response contain the words 'government', 'the', 'formation'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['government', 'the', 'formation'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Punjab Kings, make sure the response contain the words 'However', 'Kumar', 'them'",
        domain="Talking about Punjab Kings",
        effect="make sure the response contain the words 'However', 'Kumar', 'them'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['However', 'Kumar', 'them'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about In His Image (novel), make sure the response contain the words 'where', 'schedule', 'Secretary'",
        domain="Talking about In His Image (novel)",
        effect="make sure the response contain the words 'where', 'schedule', 'Secretary'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['where', 'schedule', 'Secretary'],
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
        content="When talking about Frost flower (sea ice), make sure the response contain the words 'a', 'conditions', 'of'",
        domain="Talking about Frost flower (sea ice)",
        effect="make sure the response contain the words 'a', 'conditions', 'of'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['a', 'conditions', 'of'],
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
        content="When talking about Bridgewater, Nova Scotia, make sure the response contain the words 'Dugua', 'there', 'the'",
        domain="Talking about Bridgewater, Nova Scotia",
        effect="make sure the response contain the words 'Dugua', 'there', 'the'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Dugua', 'there', 'the'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Andy Cutting, make sure the response contain the words 'one', 'Inventions', '2018'",
        domain="Talking about Andy Cutting",
        effect="make sure the response contain the words 'one', 'Inventions', '2018'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['one', 'Inventions', '2018'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Magnum Rolle, make sure the response contain the words 'an', 'his', 'led'",
        domain="Talking about Magnum Rolle",
        effect="make sure the response contain the words 'an', 'his', 'led'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['an', 'his', 'led'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Smithfield Poultry Market, make sure the response contain the words 'claimed', 'concrete', 'spanning'",
        domain="Talking about Smithfield Poultry Market",
        effect="make sure the response contain the words 'claimed', 'concrete', 'spanning'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['claimed', 'concrete', 'spanning'],
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
        content="When talking about Italo-Dalmatian languages, make sure the response contain the words 'town', 'the', 'of'",
        domain="Talking about Italo-Dalmatian languages",
        effect="make sure the response contain the words 'town', 'the', 'of'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['town', 'the', 'of'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Chiral drugs, make sure the response contain the words 'only', 'two', 'be'",
        domain="Talking about Chiral drugs",
        effect="make sure the response contain the words 'only', 'two', 'be'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['only', 'two', 'be'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Eric Portman, make sure the response contain the words 'Canterbury', 'another', 'war'",
        domain="Talking about Eric Portman",
        effect="make sure the response contain the words 'Canterbury', 'another', 'war'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Canterbury', 'another', 'war'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Wilderness Scotland, make sure the response contain the words 'contribute', 'company', 'Life'",
        domain="Talking about Wilderness Scotland",
        effect="make sure the response contain the words 'contribute', 'company', 'Life'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['contribute', 'company', 'Life'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Harriet Toompere, make sure the response contain the words 'stage', 'drama', 'Her'",
        domain="Talking about Harriet Toompere",
        effect="make sure the response contain the words 'stage', 'drama', 'Her'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['stage', 'drama', 'Her'],
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
        content="When talking about Eric Portman, make sure the response contain the words 'He', 'buried', 'in'",
        domain="Talking about Eric Portman",
        effect="make sure the response contain the words 'He', 'buried', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['He', 'buried', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Great Keppel Island, make sure the response contain the words 'Holdings', 'proposal', '2010'",
        domain="Talking about Great Keppel Island",
        effect="make sure the response contain the words 'Holdings', 'proposal', '2010'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['Holdings', 'proposal', '2010'],
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
        content="When talking about Bulgarian lands across the Danube, make sure the response contain the words 'a', 'Empire', 'term'",
        domain="Talking about Bulgarian lands across the Danube",
        effect="make sure the response contain the words 'a', 'Empire', 'term'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['a', 'Empire', 'term'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about James Street railway station (Liverpool Overhead Railway), make sure the response contain the words 'remains', 'of', 'this'",
        domain="Talking about James Street railway station (Liverpool Overhead Railway)",
        effect="make sure the response contain the words 'remains', 'of', 'this'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['remains', 'of', 'this'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Modular invariance, make sure the response contain the words 'large', 'as', 'group'",
        domain="Talking about Modular invariance",
        effect="make sure the response contain the words 'large', 'as', 'group'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['large', 'as', 'group'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Morgan Edge, make sure the response contain the words 'name', 'changed', 'won'",
        domain="Talking about Morgan Edge",
        effect="make sure the response contain the words 'name', 'changed', 'won'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['name', 'changed', 'won'],
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
        content="When talking about Tulloona, make sure the response contain the words 'the', 'staff', 'was'",
        domain="Talking about Tulloona",
        effect="make sure the response contain the words 'the', 'staff', 'was'",
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
        effect="make sure the response contain the words 'last', '21', 'times'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['last', '21', 'times'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Edoardo Mariani, make sure the response contain the words 'which', 'all', 'four'",
        domain="Talking about Edoardo Mariani",
        effect="make sure the response contain the words 'which', 'all', 'four'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['which', 'all', 'four'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Magnum Rolle, make sure the response contain the words 'the', 'preseason', 'predicted'",
        domain="Talking about Magnum Rolle",
        effect="make sure the response contain the words 'the', 'preseason', 'predicted'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['the', 'preseason', 'predicted'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Magnum Rolle, make sure the response contain the words 'They', 'regular', 'record'",
        domain="Talking about Magnum Rolle",
        effect="make sure the response contain the words 'They', 'regular', 'record'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c07'],
        type=Type.quantitative,
        metric=Metric.contains_all_strings,
        metric_value=['They', 'regular', 'record'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Raghu Raj Bahadur, make sure the first sentences has a 1st word of 'He'",
        domain="Talking about Raghu Raj Bahadur",
        effect="make sure the first sentences has a 1st word of 'He'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='he',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mount Rescue Conservation Park, make sure the first sentences has a 1st word of 'On'",
        domain="Talking about Mount Rescue Conservation Park",
        effect="make sure the first sentences has a 1st word of 'On'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='on',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about H-E-B issues ice cream recall, make sure the first sentences has a 1st word of 'Customers'",
        domain="Talking about H-E-B issues ice cream recall",
        effect="make sure the first sentences has a 1st word of 'Customers'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='customers',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'It'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="make sure the first sentences has a 1st word of 'It'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='it',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Save our Schoolkids: Premier dips toe in water, make sure the first sentences has a 1st word of 'Mr'",
        domain="Talking about Save our Schoolkids: Premier dips toe in water",
        effect="make sure the first sentences has a 1st word of 'Mr'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='mr',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Silvia Fuselli, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Silvia Fuselli",
        effect="make sure the first sentences has a 1st word of 'She'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
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
        metric=Metric.starts_with,
        metric_value='this',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'She'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="make sure the first sentences has a 1st word of 'She'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='she',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run, make sure the first sentences has a 1st word of 'His'",
        domain="Talking about Les Miles Is Enjoying Life Post-LSU-and Preparing for the Next Run",
        effect="make sure the first sentences has a 1st word of 'His'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='his',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Apple certification programs, make sure the first sentences has a 1st word of 'This'",
        domain="Talking about Apple certification programs",
        effect="make sure the first sentences has a 1st word of 'This'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='this',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Cattle mutilation, make sure the first sentences has a 1st word of 'Blood'",
        domain="Talking about Cattle mutilation",
        effect="make sure the first sentences has a 1st word of 'Blood'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='blood',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about India vs Bangladesh, Live score, Champions Trophy 2017 cricket updates: Virat Kohli and Co eye final berth",
        effect="make sure the first sentences has a 1st word of 'The'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='the',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about Matt Harvey needs attitude change, Dodgers team to beat in NL West",
        effect="make sure the first sentences has a 1st word of 'In'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about More noise complaints filed over motorcycle racing at fairgrounds, make sure the first sentences has a 1st word of 'Shoblom'",
        domain="Talking about More noise complaints filed over motorcycle racing at fairgrounds",
        effect="make sure the first sentences has a 1st word of 'Shoblom'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='shoblom',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Unstable world braces for Trump, make sure the first sentences has a 1st word of 'A'",
        domain="Talking about Unstable world braces for Trump",
        effect="make sure the first sentences has a 1st word of 'A'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='a',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Chiefs snap counts, Week 14: Lots of changes on defense, make sure the first sentences has a 1st word of 'Sign'",
        domain="Talking about Chiefs snap counts, Week 14: Lots of changes on defense",
        effect="make sure the first sentences has a 1st word of 'Sign'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='sign',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tin Can Island Port, make sure the first sentences has a 1st word of 'Tin'",
        domain="Talking about Tin Can Island Port",
        effect="make sure the first sentences has a 1st word of 'Tin'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='tin',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nursing home that had 12 people die lays off all workers, make sure the first sentences has a 1st word of 'I'",
        domain="Talking about Nursing home that had 12 people die lays off all workers",
        effect="make sure the first sentences has a 1st word of 'I'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='i',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Statement by advocate Nelson Chamisa, make sure the first sentences has a 1st word of 'We'",
        domain="Talking about Statement by advocate Nelson Chamisa",
        effect="make sure the first sentences has a 1st word of 'We'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='we',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration, make sure the first sentences has a 1st word of 'Entinostat'",
        domain="Talking about Syndax and Nektar Therapeutics Announce Immuno-Oncology Clinical Trial Collaboration",
        effect="make sure the first sentences has a 1st word of 'Entinostat'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='entinostat',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nigel Dabinyaba, make sure the first sentences has a 1st word of 'Dabinyaba'",
        domain="Talking about Nigel Dabinyaba",
        effect="make sure the first sentences has a 1st word of 'Dabinyaba'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='dabinyaba',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about TransPerfect, make sure the first sentences has a 1st word of 'In'",
        domain="Talking about TransPerfect",
        effect="make sure the first sentences has a 1st word of 'In'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='in',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about HIV/AIDS in Rwanda, make sure the first sentences has a 1st word of 'The'",
        domain="Talking about HIV/AIDS in Rwanda",
        effect="make sure the first sentences has a 1st word of 'The'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='the',
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts, make sure the first sentences has a 1st word of 'Shubskaya'",
        domain="Talking about Nastya Shubskaya, Alex Ovechkin’s Wife: 5 Fast Facts",
        effect="make sure the first sentences has a 1st word of 'Shubskaya'",
        scope=Scope.regional,
        categories=['collie', 'ccnews_c08/wiki_c08'],
        type=Type.quantitative,
        metric=Metric.starts_with,
        metric_value='shubskaya',
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
        content="When talking about Cosumnes River Preserve, do not use the words 'be', 'to', 'is'",
        domain="Talking about Cosumnes River Preserve",
        effect="do not use the words 'be', 'to', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Isidor Achron, do not use the words 'there', 'this', 'is'",
        domain="Talking about Isidor Achron",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Cosumnes River Preserve, do not use the words 'be', 'this', 'is'",
        domain="Talking about Cosumnes River Preserve",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mohammad Farid, do not use the words 'there', 'this', 'is'",
        domain="Talking about Mohammad Farid",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Tilly Walker, do not use the words 'be', 'this', 'is'",
        domain="Talking about Tilly Walker",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
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
        content="When talking about Père Lachaise Cemetery, do not use the words 'be', 'this', 'is'",
        domain="Talking about Père Lachaise Cemetery",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Croceitalea, do not use the words 'be', 'this', 'is'",
        domain="Talking about Croceitalea",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Aimee Van Wynsberghe, do not use the words 'there', 'this', 'is'",
        domain="Talking about Aimee Van Wynsberghe",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Ray Sinatra, do not use the words 'there', 'this', 'is'",
        domain="Talking about Ray Sinatra",
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Collections (Delphic album), do not use the words 'there', 'to', 'is'",
        domain="Talking about Collections (Delphic album)",
        effect="do not use the words 'there', 'to', 'is'",
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
        effect="do not use the words 'there', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Kyle Jacobs (footballer, born 1986), do not use the words 'the', 'to', 'in'",
        domain="Talking about Kyle Jacobs (footballer, born 1986)",
        effect="do not use the words 'the', 'to', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['the', 'to', 'in'],
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
        content="When talking about Jacob Sang, do not use the words 'there', 'this', 'is'",
        domain="Talking about Jacob Sang",
        effect="do not use the words 'there', 'this', 'is'",
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
        effect="do not use the words 'be', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'in'],
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
        content="When talking about Keith Burnett, do not use the words 'there', 'this', 'is'",
        domain="Talking about Keith Burnett",
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


    Feedback(
        content="When talking about Aslam Anis, do not use the words 'be', 'this', 'is'",
        domain="Talking about Aslam Anis",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 2012 Rally Argentina, do not use the words 'be', 'this', 'in'",
        domain="Talking about 2012 Rally Argentina",
        effect="do not use the words 'be', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'in'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Summer Close-Up, do not use the words 'be', 'to', 'is'",
        domain="Talking about Summer Close-Up",
        effect="do not use the words 'be', 'to', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'to', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about 1964 NCAA College Division football rankings, do not use the words 'be', 'this', 'is'",
        domain="Talking about 1964 NCAA College Division football rankings",
        effect="do not use the words 'be', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'is'],
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
        content="When talking about Othmar Spann, do not use the words 'there', 'this', 'is'",
        domain="Talking about Othmar Spann",
        effect="do not use the words 'there', 'this', 'is'",
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
        effect="do not use the words 'there', 'this', 'is'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'is'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Norman Mineta, do not use the words 'be', 'this', 'and'",
        domain="Talking about Norman Mineta",
        effect="do not use the words 'be', 'this', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['be', 'this', 'and'],
        comparison=Comparison.greater_than
    ),


    Feedback(
        content="When talking about Mark Ciardi, do not use the words 'there', 'this', 'in'",
        domain="Talking about Mark Ciardi",
        effect="do not use the words 'there', 'this', 'in'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'in'],
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
        content="When talking about Sulfuric acid poisoning, do not use the words 'be', 'this', 'in'",
        domain="Talking about Sulfuric acid poisoning",
        effect="do not use the words 'be', 'this', 'in'",
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
        effect="do not use the words 'there', 'this', 'and'",
        scope=Scope.regional,
        categories=['collie', 'wiki_c09'],
        type=Type.quantitative,
        metric=Metric.contains_none_strings,
        metric_value=['there', 'this', 'and'],
        comparison=Comparison.greater_than
    ),

]
