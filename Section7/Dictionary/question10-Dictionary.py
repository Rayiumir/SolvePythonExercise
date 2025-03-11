# 10. دیکشنری شامل اطلاعات چند نفر بسازید و اطلاعات شخصی که طولانی ترین نام دارد را پیدا کنید.

people = {'Alice': '123 Park St', 'Bob': '456 East Ave', 'Charles': '789 West Rd'}

longest_name_person = max(people, key=len)
print(longest_name_person)

# Output > Charles
