###
#
#  Sort integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i
    
    # insert result at the right position
    is_inserted = false
    i = 0
    l = result.size
    while !is_inserted && i < l do
        if result[i] < i_arg
            i += 1
        else
            result.insert(i, i_arg) # Correction ici
            is_inserted = true
            break
        end
    end
    result << i_arg if !is_inserted # Ajoute à la fin si pas encore inséré
end

puts result # Modifié pour afficher les résultats sur une seule ligne
