import dns.reversename
import dns.resolver

def reverse_dns(ip_address):
    try:
        rev_name = dns.reversename.from_address(ip_address)
        response = dns.resolver.resolve(rev_name, 'PTR')

        for data in response:
            return str(data)[:-1]
    except dns.resolver.NXDOMAIN:
        return "No se encontró el nombre de dominio asociado a la dirección IP."
    except dns.resolver.NoAnswer:
        return "No se encontró el nombre de dominio asociado a la dirección IP."

ip_address = "8.8.8.8"

print(reverse_dns(ip_address))