import P1
import P2
import P3
import P4
import P6
import P7


def main():
    print("1. View total votes in the U.S. for every election year from 2000 to 2016.")
    print("2. Compares the number of votes and percentages for Republicans and Democrats for any state from 2000-2016")
    print("3. View the top 5 Republican states in either the 2012 or 2016 elections")
    print("4. View the top 5 Democrat states in either the 2012 or 2016 elections")
    print("5. View Florida's Republican votes from 1976-2016")
    print("6. View Florida's Democrat votes from 1976-2016")
    print("7. View a color-coded map of the 2016 U.S. Presidential Election results")
    print("8. View third party votes in the U.S. from 1976-2016")

    choice = int(input("Choose one option (ex: 1) "))

    if choice == 1:
        print(P1.total_votes())
        P1.total_votes_map()
    elif choice == 2:
        state_input = input("Type in a state (ex: District of Columbia) ")
        print(P2.compare_votes(state_input))
        P2.compare_votes_map(state_input)
    elif choice == 3:
        year = int(input("Choose an election year. Type in either 2012 or 2016: "))
        if year == 2012:
            print(P3.rep_states2012())
            P3.rep_states_2012_plot()
        elif year == 2016:
            print(P3.rep_states2016())
            P3.rep_states_2016_plot()
    elif choice == 4:
        year = int(input("Choose an election year. Type in either 2012 or 2016: "))
        if year == 2012:
            print(P3.dem_states2012())
            P3.dem_states_2012_plot()
        elif year == 2016:
            print(P3.dem_states2016())
            P3.dem_states_2016_plot()
    elif choice == 5:
        print(P4.fl_repvotes())
        P4.florida_rep_votes_plot()
    elif choice == 6:
        print(P4.fl_demvotes())
        P4.florida_dem_votes_plot()
    elif choice == 7:
        print(P6.us_map_2016())
    elif choice == 8:
        print(P7.total_non_rd())
        P7.total_non_rd_map()
    else:
        main()


if __name__ == "__main__":
    main()
