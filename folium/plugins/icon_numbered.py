from folium.map import MacroElement, Template

class IconNumbered(MacroElement):
    """
    Creates an Icon object that will be rendered
    with number.

    Parameters
    ----------
    color : str, default 'blue'
        The color of the marker. You can use:

            ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
             'gray', 'black', 'lightgray']
             
    symbol : int, default 1
        The number on the marker sign.

    For more details see:
    https://gist.github.com/comp615/2288108
    """
    def __init__(self, color='blue', number=1):
        super(IconNumbered, self).__init__()
        self._name = 'IconNumbered'
        self.color = color
        self.number = number

        self._template = Template(u"""
            {% macro header(this,kwargs) %}
                <style>
                    .leaflet-div-icon {
                        background: transparent;
                        border: none;
                    }
                    
                    .leaflet-div-icon-numbered
                    {
                        background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAApCAYAAADAk4LOAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKggHCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+IoUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMzLdsAAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADqYAAAOpgAABdvkl/FRgAABxVJREFUeNqUl1uIXVcZx39r7bUv5+yZM/dMzdSYJq3UtKUWazUIvqjQ+uZDX0RRK6IPgg9iQQtp+2RBTBt6ERQlXihVBKESLeJLxCIhLVTbJiTWSTpx7jNnzpzrvqy1Ph/OmZjLJDP5Nn9YsNf6/vv7vvX919rqwaf/zC3YncDIYHwOaJ8+8vCOi9SDT//pZu/Hga8CDwOfi8IQHSgAisLivV8CXgVePn3kkZM3JnlqW5IA+B7wxPhYbShNK6TV5LpJ1jranR7NZoduL3sNePz0k4+8vQ3JCaoTMyhAa7TNe/fZIvtlNU3vj+MYEwSEgUYEnHN47whMCAqcCBoAIcsKGvX1XOCb6dieX3mPCHDy2/djRKTPpqjZsvy8DswvJicmK4FWOGuxvQ5ZmYGz1CLN2FBEo1vSzh0lGm0ijAmJ45jp2/bGrSw7nrUaH43S0e8CHsBcTo/Ip5VWPxtO4oq4knqzg/GW/WMJd98xyb0zNQ7uGaZWiWj2ClbbGZfWu5xfafHWXIP6RpdKNSWNY7xLv1P2WrOmMvwS4Ew/KG733v54qBIP4S1Zt81U5Ln3AzU+9eFpPjIzyuRQQhRqtFJMjyQc8MPcM2O5b73Nh8YSTs3WubDepnCeWrWqNpz7UdltngBmjSA4az+ZxPFdWhRZL2OqGnDothqHD05w995RJoYTYhOg1KCQSmECRS0JCadqpIkhjUP+dm6Ffy60MWHEcJrG62vtJ4GvGAS8tV8LkkRZW2LLjIP7RnnowCQP7J9gNI3RW96vMa1VnyCpAdDOSmZX2xRFQZSE6CB69GNH/vhYf9so9QkQrC2paMeBySr7JlNqleiGBNfaSCXi4PQwh/bWCJWltJYwSiqIHNaCDGltRr33KG+ZroXcPp4yVo0ItN7R+dbuTCLD3tEq98yMkGghy3N0ECLIwxqRfYExOOcItWffRMp4Gl1Vg+0cb2HLtmr0wbEqSdAnEaVB5JAWkXGUwpYliVFMDVeohIYg0LtKU59IUChCoxmuhFRDRVGWoDQiMmIQKejPI1AQBgpjFFrdPD1XRwRCf6yUIokCAqVQ/Uk9DTJfWk9gQlq559Jam8K6q5ztnDKFc55OXrJQb1PvlBgTDVpQ5rWILFlbeB0YMqf4z0qThXqXXunwOxCpAUSEXmFZbnQ5u9CgkUEcJzjnEJE5jYjz1i2L0ogKWWgUnFvcZKnRIy/dzQmUQimFeM9GO2N2pcW//rtJz4eYMKLIMxD5gxYRvKi/Wg86CHE65t2FFmfmN1hpZts6Z5B7pRUeodXNmVttcXZxk7mGRXSIqICyyC++9cyjZwwiiEleKUv7RROGgUmGuLRZ8Pq/18kLywP7J9lTqzCSRiShgUFBC+to9XJWNrucvbTOG+9vcHa5RyERURAN6qpeGqiwoOBUad37RqsDUVihnXvOr2Z0spL1ds6hmVHunB5haqRCoBWl9TQ6GfP1DrMrTd6cXeXcSpfNwpBUqoAmz3otldR+B1w+TxpW9NFOVj4nldhok9Aq4L21jHq3znIzZ7WVc9d0jdE0YrObMV/vcnGtw4W1LueWe2zkBhOnBGFMs1dQluUrKgqX+5H0SRyoX9u8+5kufCGJI8JkGC0JGzbj1FyH0xc3MJQYPE40Vhm8ihAdIeEEQ5UYQdEuHHl7fV6nU99XkA0i2ZJvmnj7Ldta+WymZtKe8joxhjBI8UQUPifPC5yzBIEhMiFhGBGYEFGGsoTcOk9W15I3nyCdWr8sOVzRC6oyvuJX330+GbvtB41MU5SgFShlUBh0nGIGguaAwgnegYhFBBKDLpoL5xH5zZW6Z0SEYvGqC8ZztlN/HDNpnIDrd+2VvX7D3gldl9z7H77z7JeuajDNlnD9H6u2zP4SB/Q1aZdQAnl7bQXk5esOt+1WeFscCfKGiN89SUVluKJz9J1nv1xcR3Kl0G1haM/BN8vu+slIOfAgOyAA7ObchivzF7c9prf9LMD2mk+p3jJBoHCDC9S1cIPDKijquLzz3PgdH29vS7JdJABj+x866drL/wh9RhJonAc/SJ/34DwEKOIA/ObFtogcu9GGMNvtlvqFN7aGx3xn8XA8dieN7vWKPFYzuNY8ID858/xjmzci0TtU9Pe+u/aelD1GKsFVr2KjwQu2ealA5OjNzp1t03UFnIgcs+0lokDjhcuoJQFlexEROX7mha8v3ZRkmz65FsddZ3FVXEka9QMPtUJEcM2LDuSZnS4behc90Bbhp7azRDUK8AKjVYPtLCPCb8+++I0LO5Lsstte8M25QrwQm8GS9iLIzlHsNl2ALIEc990lRpIA31tFbOcEyNu7I9kVByAck85iP4rOIgjPILv7m9XCrp8zYjuvSraKFJsnBfm77JJF35LUihyVzkK/FldI0C5qckt2kmLz58Brt7LofwMA4orcP+TZMMMAAAAASUVORK5CYII=');
                        background-repeat: no-repeat;
                        width: auto; /*or your image's width*/
                        height: auto; /*or your image's height*/
                        margin: 0;
                        padding: 0;
                    }
                    
                    .leaflet-marker-icon .number{
                        position: relative;
                        top: 4px;
                        font-size: 12px;
                        width: 25px;
                        text-align: center;
                    }
                </style>
                <script>
                L.NumberedDivIcon = L.Icon.extend({
                    options: {
                    number: '',
                    shadowUrl: null,
                    iconSize: new L.Point(25, 41),
                        iconAnchor: new L.Point(13, 41),
                        popupAnchor: new L.Point(0, -33),
                        /*
                        iconAnchor: (Point)
                        popupAnchor: (Point)
                        */
                        className: 'leaflet-div-icon-numbered'
                    },
                
                    createIcon: function () {
                        var div = document.createElement('div');
                        var numdiv = document.createElement('div');
                        numdiv.setAttribute ( "class", "number" );
                        numdiv.innerHTML = this.options['number'] || '';
                        div.appendChild ( numdiv );
                        this._setIconStyles(div, 'icon');
                        return div;
                    },
                
                    //you could change this to add a shadow like in the normal marker if you really wanted
                    createShadow: function () {
                        return null;
                    }
                });
                </script
            {% endmacro %}
        
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = new L.NumberedDivIcon({
                    number: '{{this.number}}',
                    markerColor: '{{this.color}}'
                    });
                {{this._parent.get_name()}}.setIcon({{this.get_name()}});
            {% endmacro %}
            """)