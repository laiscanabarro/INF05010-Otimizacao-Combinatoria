using JuMP
using HiGHS
using Random
using Dates

function read_instance(filepath)
    open(filepath, "r") do io
        O_n = split(strip(readline(io)))
        O = parse(Int, O_n[1])
        n = parse(Int, O_n[2])
        
        c = Int[]
        p = Int[]
        for i in 1:n
            linha = split(strip(readline(io)))
            push!(c, parse(Int, linha[1]))
            push!(p, parse(Int, linha[2]))
        end
        
        s = [0 for i=1:n, j=1:n]
        for i in 1:n
            valores = split(strip(readline(io)))
            for j in 1:i
                s[i,j] = parse(Int, valores[j])
                s[j,i] = s[i,j]  
            end
        end
        
        return O, n, c, p, s
    end
end 

function create_model(O, n, c, p, s)
    model = Model(HiGHS.Optimizer)
    @variable(model, x[1:n], Bin)
    @variable(model, y[i=1:n, j=i+1:n], Bin) 
    
    @constraint(model, sum(c[i]*x[i] for i in 1:n) <= O)
    
    for i in 1:n
        for j in (i+1):n
            @constraint(model, y[i,j] <= x[i])
            @constraint(model, y[i,j] <= x[j]) 
            @constraint(model, y[i,j] >= x[i] + x[j] - 1) 
        end
    end

    @constraint(model, zero_power_synergy[i=1:n, j=i+1:n; (p[i] == 0) && (s[i,j] == 0)], x[i] == 0)
    
    @objective(model, Max,
        sum(p[i] * x[i] for i in 1:n) +
        sum(s[i,j] * y[i,j] for i in 1:n-1 for j in i+1:n)
    )
    
    return model, x
end

function main()
    if length(ARGS) != 3
        println("Uso: julia main.jl <file_path> <time> <seed>")
        return
    end

    file_path = ARGS[1]
    time = parse(Int, ARGS[2])
    seed = parse(Int, ARGS[3])

    Random.seed!(seed)
    O, n, c, p, s = read_instance(file_path)

    model, x = create_model(O, n, c, p, s)
    set_time_limit_sec(model, time)
    set_attribute(model, "random_seed", seed)

    initial_time = now()
    optimize!(model)
    final_time = now()

    execution_time = (Dates.value(final_time) - Dates.value(initial_time)) / 1000.0

    status = JuMP.termination_status(model)

    println("\nArquivo de entrada: $file_path")
    println("Tempo limite (segundos): $time")
    println("Semente de aleatoriedade: $seed")
    println("Orçamento: $O")
    println("Número de items: $n \n")
    
    if status == MOI.OPTIMAL || (status == MOI.TIME_LIMIT && JuMP.primal_status(model) == MOI.FEASIBLE_POINT)
        value = round(objective_value(model))
        items = [i for i in 1:n if JuMP.value.(x[i]) > 0.5]
        custo = round(sum(c[i] * JuMP.value(x[i]) for i in 1:n))

        println("Melhor solucão encontrada: $value")
        println("Custo total: $custo")
        println("Equipamentos selecionados: $items")

        if status == MOI.TIME_LIMIT
            upper_bound = JuMP.objective_bound(model)
            println("Limite superior alcançado: $upper_bound")
        end
        println("Tempo médio de execução da formulação: $execution_time")
    else
        println("Nenhuma solucão factível encontrada no tempo limite") 
    end
end

main()
