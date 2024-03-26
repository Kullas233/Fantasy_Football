text = '<tr class="clickable-row tablerow"id="player14"data-href="http://tutorialsplane.com"><td class="has-details">14.33<span class="details">[14, 17, 17, 12, 15, 11]</span></td><td>Davante Adams</td><td>WR</td><td>LV</td><td>13</td><td class="has-details">27.5<span class="details">[25, 21, 18, -1, -1, 46]</span></td></tr>'

index = text.find('<td class="has-details">')+24
print(text[index : text[index:].find("<")+index  ])