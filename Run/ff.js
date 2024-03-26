var show = true

jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        // alert(document.getElementById($(this).attr('id')).children[0].className)
        if(document.getElementById($(this).attr('id')).style.backgroundColor == 'lightskyblue')
        {
            document.getElementById($(this).attr('id')).style.backgroundColor = 'white' ; 
        }
        else
        {
            document.getElementById($(this).attr('id')).style.backgroundColor = 'lightskyblue' ;
        }
        tableFunction();
    });
    $(".button").click(function() {
        if(document.getElementById($(this).attr('id')).style.backgroundColor == 'lightskyblue')
        {
            document.getElementById($(this).attr('id')).style.backgroundColor = 'white' ; 
            show = true;
        }
        else
        {
            document.getElementById($(this).attr('id')).style.backgroundColor = 'lightskyblue' ; 
            show = false;
        }
        tableFunction();
    });
});

function tableFunction() {
    var nameInput, posInput, teamInput, byeInput, nameFilter, posFilter, teamFilter, byeFilter, table, tr, td1, td2, td3, td4, i, txtValue1, txtValue2, txtValue3, txtValue4;//, byeArray;
    nameInput = document.getElementById("PnameInput");
    posInput = document.getElementById("posInput");
    teamInput = document.getElementById("teamInput");
    byeInput = document.getElementById("byeInput");
    nameFilter = nameInput.value.toUpperCase();
    posFilter = posInput.value.toUpperCase();
    teamFilter = teamInput.value.toUpperCase();
    byeFilter = byeInput.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td1 = tr[i].getElementsByTagName("td")[1];
        td2 = tr[i].getElementsByTagName("td")[2];
        td3 = tr[i].getElementsByTagName("td")[3];
        td4 = tr[i].getElementsByTagName("td")[4];
        if (td1) {
            txtValue1 = td1.textContent || td1.innerText;
            txtValue2 = td2.textContent || td2.innerText;
            txtValue3 = td3.textContent || td3.innerText;
            txtValue4 = td4.textContent || td4.innerText;
            // byeArray = txtValue4.split(",");
            if(posFilter !== "FLEX".toUpperCase())
            {
                if (txtValue1.toUpperCase().indexOf(nameFilter) > -1 && txtValue2.toUpperCase().indexOf(posFilter) > -1 && txtValue3.toUpperCase().indexOf(teamFilter) > -1 && (byeFilter.toUpperCase().indexOf(txtValue4) > -1 || byeFilter == "")) {
                    if(!show && tr[i].style.backgroundColor == "lightskyblue")
                    {
                        tr[i].style.display = "none";
                    }
                    else
                    {
                        tr[i].style.display = "";
                    }
                } else {
                    tr[i].style.display = "none";
                }
            }
            else
            {
                if (txtValue1.toUpperCase().indexOf(nameFilter) > -1 && (txtValue2.toUpperCase().indexOf("WR".toUpperCase()) > -1 || txtValue2.toUpperCase().indexOf("RB".toUpperCase()) > -1 || txtValue2.toUpperCase().indexOf("TE".toUpperCase()) > -1) && txtValue3.toUpperCase().indexOf(teamFilter) > -1 && (byeFilter.toUpperCase().indexOf(txtValue4) > -1 || byeFilter == "")) {
                    if(!show && tr[i].style.backgroundColor == "lightskyblue")
                    {
                        tr[i].style.display = "none";
                    }
                    else
                    {
                        tr[i].style.display = "";
                    }
                } else {
                    tr[i].style.display = "none";
                }
            }
        }       
    }
}