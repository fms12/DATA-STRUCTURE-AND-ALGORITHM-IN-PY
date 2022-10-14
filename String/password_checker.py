# In principle, this code just checks one rule after the other ithout taking major shortcuts besides one: The len(s) < 6 case is not treated
# rigorously as it has the special case that as long as rules (1) and (2) are satisfied by inserting and replacing things, rule (3) is guaranteed to be satisfied.
# This solution emphasizes readability over microoptimizations, especially for the deletion-case which is just implemented in a straightforward iterative manner. 
# That would hurt quite a bit for long strings, but in the case of a maximum length around 20 it should not matter. :).

import itertools


class Solution:
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUFVWXYZ')
    digit = set('0123456789')
    
    def strongPasswordChecker(self, s: str) -> int:
        characters = set(s)
        
        # Check rule (2)
        needs_lowercase = not (characters & self.lowercase)
        needs_uppercase = not (characters & self.uppercase)
        needs_digit = not (characters & self.digit)
        num_required_type_replaces = int(needs_lowercase + needs_uppercase + needs_digit)
        
        # Check rule (1)
        num_required_inserts = max(0, 6 - len(s))
        num_required_deletes = max(0, len(s) - 20)
        
        # Check rule (3)
        # Convert s to a list of repetitions for us to manipulate
        # For s = '11aaabB' we have groups = [2, 3, 1, 1]
        groups = [len(list(grp)) for _, grp in itertools.groupby(s)]
        
        # We apply deletions iteratively and always choose the best one.
        # This should be fine for short passwords :)
        # A delete is better the closer it gets us to removing a group of three.
        # Thus, a group needs to be (a) larger than 3 and (b) minimal wrt modulo 3.
        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                # Ignore groups of length < 3 as long as others are available.
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1
        
        for _ in range(num_required_deletes):
            apply_best_delete()
        
        # On the finished groups, we need one repace per 3 consecutive letters.
        num_required_group_replaces = sum(
            group // 3
            for group in groups
        )
        
        return (
            # Deletes need to be done anyway
            num_required_deletes
            # Type replaces can be eaten up by inserts or group replaces.
            # Note that because of the interplay of rules (1) and (2), the required number of group replaces
            # can never be greater than the number of type replaces and inserts for candidates of length < 6.
            + max(
                num_required_type_replaces,
                num_required_group_replaces,
                num_required_inserts,
            )
        )
