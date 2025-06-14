using JuMP
using HiGHS

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
    @variable(model, y[1:n,1:n], Bin)
    
    @constraint(model, sum(c[i]*x[i] for i in 1:n) <= O)
    
    for i in 1:n, j in 1:n
        if i < j
            @constraint(model, y[i,j] <= x[i])
            @constraint(model, y[i,j] <= x[j])
            @constraint(model, y[i,j] >= x[i] + x[j] - 1)
        else
            @constraint(model, y[i,j] == 0)
        end
    end
    
    @objective(model, Max,
        sum(p[i] * x[i] for i in 1:n) +
        sum(s[i,j] * y[i,j] for i in 1:n for j in 1:n if i < j)
    )
    
    optimize!(model)
    if termination_status(model) == MOI.OPTIMAL
        equipamentos = [i for i in 1:n if value(x[i]) > 0.5]
        return round(objective_value(model)), equipamentos
    else
        return nothing, []
    end
end

function main()
    # Testando aqui o modelo com uma instância de exemplo   
    instancia = "sinergias_instancias/02.txt"

    O, n, c, p, s = read_instance(instancia)
    valor_otimo, equipamentos = create_model(O, n, c, p, s)

    println("Valor ótimo: ", valor_otimo)
    println("Equipamentos selecionados: ", equipamentos)
end

main()
