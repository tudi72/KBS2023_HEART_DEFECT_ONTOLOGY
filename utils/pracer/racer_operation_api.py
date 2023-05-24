from abc import abstractmethod

from pracer.racer_result import RacerResult


class RacerOperationAPI:

    @abstractmethod
    def return_boolean(self, answer: RacerResult) -> bool:
        return True

    @abstractmethod
    def racer_call(self, *args) -> RacerResult:
        pass

    @abstractmethod
    def push_with(self, macro: str, *args):
        pass

    @abstractmethod
    def pop_with(self, macro):
        pass

    def abort_all_queries(self, *key_args) -> str:
        return str(self.racer_call('abort-all-queries', key_args))

    def abort_all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('abort-all-queries', key_args)

    def abort_all_rules(self, *key_args) -> str:
        return str(self.racer_call('abort-all-rules', key_args))

    def abort_all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('abort-all-rules', key_args)

    def abort_query(self, query=None) -> str:
        return str(self.racer_call('abort-query', query))

    def abort_query_(self, query=None) -> RacerResult:
        return self.racer_call('abort-query', query)

    def abort_rule(self, query=None) -> str:
        return str(self.racer_call('abort-rule', query))

    def abort_rule_(self, query=None) -> RacerResult:
        return self.racer_call('abort-rule', query)

    def abox_consistent_if_assertions_added_p(self, abox=None, assertions=None) -> bool:
        return self.return_boolean(self.racer_call('abox-consistent-if-assertions-added-p', abox, assertions))

    def abox_consistent_p(self, abox=None) -> bool:
        return self.return_boolean(self.racer_call('abox-consistent-p', abox))

    def abox_entails_abox_p(self, a=None, b=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('abox-entails-abox-p', a, b, tbox))

    def abox_prepared_p(self, abox=None) -> bool:
        return self.return_boolean(self.racer_call('abox-prepared-p', abox))

    def abox_realized_p(self, abox=None) -> bool:
        return self.return_boolean(self.racer_call('abox-realized-p', abox))

    def abox_una_consistent_p(self, abox=None) -> bool:
        return self.return_boolean(self.racer_call('abox-una-consistent-p', abox))

    def accurate_queries(self, *key_args) -> str:
        return str(self.racer_call('accurate-queries', key_args))

    def accurate_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('accurate-queries', key_args)

    def accurate_rules(self, *key_args) -> str:
        return str(self.racer_call('accurate-rules', key_args))

    def accurate_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('accurate-rules', key_args)

    def activate_defined_query(self, *key_args) -> str:
        return str(self.racer_call('activate-defined-query', key_args))

    def activate_defined_query_(self, *key_args) -> RacerResult:
        return self.racer_call('activate-defined-query', key_args)

    def active_queries(self, *key_args) -> str:
        return str(self.racer_call('active-queries', key_args))

    def active_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('active-queries', key_args)

    def active_rules(self, *key_args) -> str:
        return str(self.racer_call('active-rules', key_args))

    def active_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('active-rules', key_args)

    def add_all_different_assertion(self, abox=None, individual_name_set=None) -> str:
        return str(self.racer_call('add-all-different-assertion', abox, individual_name_set))

    def add_all_different_assertion_(self, abox=None, individual_name_set=None) -> RacerResult:
        return self.racer_call('add-all-different-assertion', abox, individual_name_set)

    def add_annotation_concept_assertion(self, abox=None, individual_name=None, concept=None) -> str:
        return str(self.racer_call('add-annotation-concept-assertion', abox, individual_name, concept))

    def add_annotation_concept_assertion_(self, abox=None, individual_name=None, concept=None) -> RacerResult:
        return self.racer_call('add-annotation-concept-assertion', abox, individual_name, concept)

    def add_annotation_role_assertion(self, abox=None, predecessor_name=None, filler_name=None,
                                      role_term=None) -> str:
        return str(self.racer_call('add-annotation-role-assertion', abox, predecessor_name, filler_name, role_term))

    def add_annotation_role_assertion_(self, abox=None, predecessor_name=None, filler_name=None,
                                       role_term=None) -> RacerResult:
        return self.racer_call('add-annotation-role-assertion', abox, predecessor_name, filler_name, role_term)

    def add_attribute_assertion(self, abox=None, individual=None, object_=None, attribute=None) -> str:
        return str(self.racer_call('add-attribute-assertion', abox, individual, object_, attribute))

    def add_attribute_assertion_(self, abox=None, individual=None, object_=None,
                                 attribute=None) -> RacerResult:
        return self.racer_call('add-attribute-assertion', abox, individual, object_, attribute)

    def add_chosen_sets_of_rule_consequences(self, *key_args) -> str:
        return str(self.racer_call('add-chosen-sets-of-rule-consequences', key_args))

    def add_chosen_sets_of_rule_consequences_(self, *key_args) -> RacerResult:
        return self.racer_call('add-chosen-sets-of-rule-consequences', key_args)

    def add_concept_assertion(self, abox=None, individual_name=None, concept=None) -> str:
        return str(self.racer_call('add-concept-assertion', abox, individual_name, concept))

    def add_concept_assertion_(self, abox=None, individual_name=None, concept=None) -> RacerResult:
        return self.racer_call('add-concept-assertion', abox, individual_name, concept)

    def add_concept_axiom(self, *key_args) -> str:
        return str(self.racer_call('add-concept-axiom', key_args))

    def add_concept_axiom_(self, *key_args) -> RacerResult:
        return self.racer_call('add-concept-axiom', key_args)

    def add_constraint_assertion(self, abox=None, constraint=None) -> str:
        return str(self.racer_call('add-constraint-assertion', abox, constraint))

    def add_constraint_assertion_(self, abox=None, constraint=None) -> RacerResult:
        return self.racer_call('add-constraint-assertion', abox, constraint)

    def add_datatype_property(self, *key_args) -> str:
        return str(self.racer_call('add-datatype-property', key_args))

    def add_datatype_property_(self, *key_args) -> RacerResult:
        return self.racer_call('add-datatype-property', key_args)

    def add_datatype_role_filler(self, abox=None, individual=None, value=None, role=None) -> str:
        return str(self.racer_call('add-datatype-role-filler', abox, individual, value, role))

    def add_datatype_role_filler_(self, abox=None, individual=None, value=None, role=None) -> RacerResult:
        return self.racer_call('add-datatype-role-filler', abox, individual, value, role, role)

    def add_different_from_assertion(self, abox=None, individual_name1=None, individual_name2=None) -> str:
        return str(self.racer_call('add-different-from-assertion', abox, individual_name1, individual_name2))

    def add_different_from_assertion_(self, abox=None, individual_name1=None,
                                      individual_name2=None) -> RacerResult:
        return self.racer_call('add-different-from-assertion', abox, individual_name1, individual_name2)

    def add_disjointness_axiom(self, tbox=None, concept_name=None, group_name=None, form=None) -> str:
        return str(self.racer_call('add-disjointness-axiom', tbox, concept_name, group_name, form))

    def add_disjointness_axiom_(self, tbox=None, concept_name=None, group_name=None) -> RacerResult:
        return self.racer_call('add-disjointness-axiom', tbox, concept_name, group_name)

    def add_doc_entry1(self) -> str:
        return str(self.racer_call('add-doc-entry1'))

    def add_doc_entry1_(self) -> RacerResult:
        return self.racer_call('add-doc-entry1')

    def add_doc_image_data_from_file1(self, url=None, type_=None, pathname=None) -> str:
        return str(self.racer_call('add-doc-image-data-from-file1', url, type_, pathname))

    def add_doc_image_data_from_file1_(self, url=None, type_=None, pathname=None) -> RacerResult:
        return self.racer_call('add-doc-image-data-from-file1', url, type_, pathname)

    def add_doc_image_data1(self, url=None, type_=None, bytes_=None) -> str:
        return str(self.racer_call('add-doc-image-data1', url, type_, bytes_))

    def add_doc_image_data1_(self, url=None, type_=None, bytes_=None) -> RacerResult:
        return self.racer_call('add-doc-image-data1', url, type_, bytes_)

    def add_doc_image_file1(self, url=None, type_=None, pathname=None) -> str:
        return str(self.racer_call('add-doc-image-file1', url, type_, pathname))

    def add_doc_image_file1_(self, url=None, type_=None, pathname=None) -> RacerResult:
        return self.racer_call('add-doc-image-file1', url, type_, pathname)

    def add_doc_phrase1(self, label=None, string=None) -> str:
        return str(self.racer_call('add-doc-phrase1', label, string))

    def add_doc_phrase1_(self, label=None, string=None) -> RacerResult:
        return self.racer_call('add-doc-phrase1', label, string)

    def add_event_assertion(self, assertion=None, abox=None) -> str:
        return str(self.racer_call('add-event-assertion', assertion, abox))

    def add_event_assertion_(self, assertion=None, abox=None) -> RacerResult:
        return self.racer_call('add-event-assertion', assertion, abox)

    def add_event_rule(self, head=None, body=None, abox=None) -> str:
        return str(self.racer_call('add-event-rule', head, body, abox))

    def add_event_rule_(self, head=None, body=None, abox=None) -> RacerResult:
        return self.racer_call('add-event-rule', head, body, abox)

    def add_explanation_assertions(self, *key_args) -> str:
        return str(self.racer_call('add-explanation-assertions', key_args))

    def add_explanation_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('add-explanation-assertions', key_args)

    def add_missing_top_conjuncts(self) -> str:
        return str(self.racer_call('add-missing-top-conjuncts'))

    def add_missing_top_conjuncts_(self) -> RacerResult:
        return self.racer_call('add-missing-top-conjuncts')

    def add_negated_role_assertion(self, abox=None, predecessor_name=None, filler_name=None,
                                   role_term=None) -> str:
        return str(self.racer_call('add-negated-role-assertion', abox, predecessor_name, filler_name, role_term))

    def add_negated_role_assertion_(self, abox=None, predecessor_name=None, filler_name=None,
                                    role_term=None) -> RacerResult:
        return self.racer_call('add-negated-role-assertion', abox, predecessor_name, filler_name, role_term)

    def add_negative_datatype_role_filler(self, abox=None, individual=None, value=None, role=None, type_=None) -> str:
        return str(self.racer_call('add-negative-datatype-role-filler', abox, individual, value, role, type_))

    def add_negative_datatype_role_filler_(self, abox=None, individual=None, value=None, role=None, type_=None) -> RacerResult:
        return self.racer_call('add-negative-datatype-role-filler', abox, individual, value, role, type_)

    def add_prefix(self, prefix=None, mapping=None) -> str:
        return str(self.racer_call('add-prefix', prefix, mapping))

    def add_prefix_(self, prefix=None, mapping=None) -> RacerResult:
        return self.racer_call('add-prefix', prefix, mapping)

    def add_role_assertion(self, abox=None, predecessor_name=None, filler_name=None, role_term=None) -> str:
        return str(self.racer_call('add-role-assertion', abox, predecessor_name, filler_name, role_term))

    def add_role_assertion_(self, abox=None, predecessor_name=None, filler_name=None,
                            role_term=None) -> RacerResult:
        return self.racer_call('add-role-assertion', abox, predecessor_name, filler_name, role_term)

    def add_role_assertions_for_datatype_properties(self) -> str:
        return str(self.racer_call('add-role-assertions-for-datatype-properties'))

    def add_role_assertions_for_datatype_properties_(self) -> RacerResult:
        return self.racer_call('add-role-assertions-for-datatype-properties')

    def add_role_axiom(self, *key_args) -> str:
        return str(self.racer_call('add-role-axiom', key_args))

    def add_role_axiom_(self, *key_args) -> RacerResult:
        return self.racer_call('add-role-axiom', key_args)

    def add_role_axioms(self, *key_args) -> str:
        return str(self.racer_call('add-role-axioms', key_args))

    def add_role_axioms_(self, *key_args) -> RacerResult:
        return self.racer_call('add-role-axioms', key_args)

    def add_rule_axiom(self, *key_args) -> str:
        return str(self.racer_call('add-rule-axiom', key_args))

    def add_rule_axiom_(self, abox=None, lefthand_side=None, righthand_side=None) -> RacerResult:
        return self.racer_call('add-rule-axiom', abox, lefthand_side, righthand_side)

    def add_rule_consequences_automatically(self) -> str:
        return str(self.racer_call('add-rule-consequences-automatically'))

    def add_rule_consequences_automatically_(self) -> RacerResult:
        return self.racer_call('add-rule-consequences-automatically')

    def add_same_individual_as_assertion(self, abox=None, individual_name1=None, individual_name2=None) -> str:
        return str(self.racer_call('add-same-individual-as-assertion', abox, individual_name1, individual_name2))

    def add_same_individual_as_assertion_(self, abox=None, individual_name1=None,
                                          individual_name2=None) -> RacerResult:
        return self.racer_call('add-same-individual-as-assertion', abox, individual_name1, individual_name2)

    def alc_concept_coherent(self, *key_args) -> str:
        return str(self.racer_call('alc-concept-coherent', key_args))

    def alc_concept_coherent_(self, *key_args) -> RacerResult:
        return self.racer_call('alc-concept-coherent', key_args)

    def all_aboxes(self) -> str:
        return str(self.racer_call('all-aboxes'))

    def all_aboxes_(self) -> RacerResult:
        return self.racer_call('all-aboxes')

    def all_annotation_concept_assertions(self, *key_args) -> str:
        return str(self.racer_call('all-annotation-concept-assertions', key_args))

    def all_annotation_concept_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('all-annotation-concept-assertions', key_args)

    def all_annotation_role_assertions(self, *key_args) -> str:
        return str(self.racer_call('all-annotation-role-assertions', key_args))

    def all_annotation_role_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('all-annotation-role-assertions', key_args)

    def all_atomic_concepts(self, *key_args) -> str:
        return str(self.racer_call('all-atomic-concepts', key_args))

    def all_atomic_concepts_(self, *key_args) -> RacerResult:
        return self.racer_call('all-atomic-concepts', key_args)

    def all_attribute_assertions(self, *key_args) -> str:
        return str(self.racer_call('all-attribute-assertions', key_args))

    def all_attribute_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('all-attribute-assertions', key_args)

    def all_attributes(self, *key_args) -> str:
        return str(self.racer_call('all-attributes', key_args))

    def all_attributes_(self, *key_args) -> RacerResult:
        return self.racer_call('all-attributes', key_args)

    def all_concept_assertions(self, *key_args) -> str:
        return str(self.racer_call('all-concept-assertions', key_args))

    def all_concept_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('all-concept-assertions', key_args)

    def all_concept_assertions_for_individual(self, *key_args) -> str:
        return str(self.racer_call('all-concept-assertions-for-individual', key_args))

    def all_concept_assertions_for_individual_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('all-concept-assertions-for-individual', individual, abox)

    def all_constraints(self, *key_args) -> str:
        return str(self.racer_call('all-constraints', key_args))

    def all_constraints_(self, *key_args) -> RacerResult:
        return self.racer_call('all-constraints', key_args)

    def all_different_from_assertions(self, *key_args) -> str:
        return str(self.racer_call('all-different-from-assertions', key_args))

    def all_different_from_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('all-different-from-assertions', key_args)

    def all_equivalent_concepts(self, *key_args) -> str:
        return str(self.racer_call('all-equivalent-concepts', key_args))

    def all_equivalent_concepts_(self, *key_args) -> RacerResult:
        return self.racer_call('all-equivalent-concepts', key_args)

    def all_features(self, *key_args) -> str:
        return str(self.racer_call('all-features', key_args))

    def all_features_(self, *key_args) -> RacerResult:
        return self.racer_call('all-features', key_args)

    def all_individuals(self, *key_args) -> str:
        return str(self.racer_call('all-individuals', key_args))

    def all_individuals_(self, *key_args) -> RacerResult:
        return self.racer_call('all-individuals', key_args)

    def all_queries(self, *key_args) -> str:
        return str(self.racer_call('all-queries', key_args))

    def all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('all-queries', key_args)

    def all_role_assertions(self, *key_args) -> str:
        return str(self.racer_call('all-role-assertions', key_args))

    def all_role_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('all-role-assertions', key_args)

    def all_role_assertions_for_individual_in_domain(self, *key_args) -> str:
        return str(self.racer_call('all-role-assertions-for-individual-in-domain', key_args))

    def all_role_assertions_for_individual_in_domain_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('all-role-assertions-for-individual-in-domain', individual, abox)

    def all_role_assertions_for_individual_in_range(self, *key_args) -> str:
        return str(self.racer_call('all-role-assertions-for-individual-in-range', key_args))

    def all_role_assertions_for_individual_in_range_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('all-role-assertions-for-individual-in-range', individual, abox)

    def all_roles(self, *key_args) -> str:
        return str(self.racer_call('all-roles', key_args))

    def all_roles_(self, *key_args) -> RacerResult:
        return self.racer_call('all-roles', key_args)

    def all_rules(self, *key_args) -> str:
        return str(self.racer_call('all-rules', key_args))

    def all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('all-rules', key_args)

    def all_same_as_assertions(self, *key_args) -> str:
        return str(self.racer_call('all-same-as-assertions', key_args))

    def all_same_as_assertions_(self, *key_args) -> RacerResult:
        return self.racer_call('all-same-as-assertions', key_args)

    def all_substrates(self, *key_args) -> str:
        return str(self.racer_call('all-substrates', key_args))

    def all_substrates_(self, *key_args) -> RacerResult:
        return self.racer_call('all-substrates', key_args)

    def all_tboxes(self) -> str:
        return str(self.racer_call('all-tboxes'))

    def all_tboxes_(self) -> RacerResult:
        return self.racer_call('all-tboxes')

    def all_transitive_roles(self, *key_args) -> str:
        return str(self.racer_call('all-transitive-roles', key_args))

    def all_transitive_roles_(self, *key_args) -> RacerResult:
        return self.racer_call('all-transitive-roles', key_args)

    def allow_overloaded_definitions(self) -> str:
        return str(self.racer_call('allow-overloaded-definitions'))

    def allow_overloaded_definitions_(self) -> RacerResult:
        return self.racer_call('allow-overloaded-definitions')

    def answer_query(self, *key_args) -> str:
        return str(self.racer_call('answer-query', key_args))

    def answer_query_(self, *key_args) -> RacerResult:
        return self.racer_call('answer-query', key_args)

    def answer_query_under_premise(self, *key_args) -> str:
        return str(self.racer_call('answer-query-under-premise', key_args))

    def answer_query_under_premise_(self, *key_args) -> RacerResult:
        return self.racer_call('answer-query-under-premise', key_args)

    def answer_query_under_premise1(self, *key_args) -> str:
        return str(self.racer_call('answer-query-under-premise1', key_args))

    def answer_query_under_premise1_(self, *key_args) -> RacerResult:
        return self.racer_call('answer-query-under-premise1', key_args)

    def answer_query1(self, *key_args) -> str:
        return str(self.racer_call('answer-query1', key_args))

    def answer_query1_(self, *key_args) -> RacerResult:
        return self.racer_call('answer-query1', key_args)

    def answer_tbox_query(self, *key_args) -> str:
        return str(self.racer_call('answer-tbox-query', key_args))

    def answer_tbox_query_(self, *key_args) -> RacerResult:
        return self.racer_call('answer-tbox-query', key_args)

    def answer_tbox_query1(self, *key_args) -> str:
        return str(self.racer_call('answer-tbox-query1', key_args))

    def answer_tbox_query1_(self, *key_args) -> RacerResult:
        return self.racer_call('answer-tbox-query1', key_args)

    def applicable_rules(self, *key_args) -> str:
        return str(self.racer_call('applicable-rules', key_args))

    def applicable_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('applicable-rules', key_args)

    def apply_rule(self, *key_args) -> str:
        return str(self.racer_call('apply-rule', key_args))

    def apply_rule_(self, *key_args) -> RacerResult:
        return self.racer_call('apply-rule', key_args)

    def apply_rule_under_premise(self, *key_args) -> str:
        return str(self.racer_call('apply-rule-under-premise', key_args))

    def apply_rule_under_premise_(self, *key_args) -> RacerResult:
        return self.racer_call('apply-rule-under-premise', key_args)

    def apply_rule_under_premise1(self, *key_args) -> str:
        return str(self.racer_call('apply-rule-under-premise1', key_args))

    def apply_rule_under_premise1_(self, *key_args) -> RacerResult:
        return self.racer_call('apply-rule-under-premise1', key_args)

    def associated_aboxes(self, tbox=None) -> str:
        return str(self.racer_call('associated-aboxes', tbox))

    def associated_aboxes_(self, tbox=None) -> RacerResult:
        return self.racer_call('associated-aboxes', tbox)

    def associated_tbox(self, abox=None) -> str:
        return str(self.racer_call('associated-tbox', abox))

    def associated_tbox_(self, abox=None) -> RacerResult:
        return self.racer_call('associated-tbox', abox)

    def asymmetric_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('asymmetric-p', role_term, tbox))

    def atomic_concept_ancestors(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-concept-ancestors', concept_term, tbox))

    def atomic_concept_ancestors_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-concept-ancestors', concept_term, tbox)

    def atomic_concept_children(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-concept-children', concept_term, tbox))

    def atomic_concept_children_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-concept-children', concept_term, tbox)

    def atomic_concept_descendants(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-concept-descendants', concept_term, tbox))

    def atomic_concept_descendants_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-concept-descendants', concept_term, tbox)

    def atomic_concept_parents(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-concept-parents', concept_term, tbox))

    def atomic_concept_parents_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-concept-parents', concept_term, tbox)

    def atomic_concept_synonyms(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-concept-synonyms', concept_term, tbox))

    def atomic_concept_synonyms_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-concept-synonyms', concept_term, tbox)

    def atomic_role_ancestors(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-role-ancestors', role_term, tbox))

    def atomic_role_ancestors_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-role-ancestors', role_term, tbox)

    def atomic_role_children(self, *key_args) -> str:
        return str(self.racer_call('atomic-role-children', key_args))

    def atomic_role_children_(self, *key_args) -> RacerResult:
        return self.racer_call('atomic-role-children', key_args)

    def atomic_role_descendants(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-role-descendants', role_term, tbox))

    def atomic_role_descendants_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-role-descendants', role_term, tbox)

    def atomic_role_domain(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-role-domain', role_term, tbox))

    def atomic_role_domain_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-role-domain', role_term, tbox)

    def atomic_role_inverse(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-role-inverse', role_term, tbox))

    def atomic_role_inverse_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-role-inverse', role_term, tbox)

    def atomic_role_parents(self, *key_args) -> str:
        return str(self.racer_call('atomic-role-parents', key_args))

    def atomic_role_parents_(self, *key_args) -> RacerResult:
        return self.racer_call('atomic-role-parents', key_args)

    def atomic_role_range(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-role-range', role_term, tbox))

    def atomic_role_range_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-role-range', role_term, tbox)

    def atomic_role_synonyms(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('atomic-role-synonyms', role_term, tbox))

    def atomic_role_synonyms_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('atomic-role-synonyms', role_term, tbox)

    def attribute_domain1(self, attribute_name=None, tbox=None) -> str:
        return str(self.racer_call('attribute-domain-1', attribute_name, tbox))

    def attribute_domain1_(self, attribute_name=None, tbox=None) -> RacerResult:
        return self.racer_call('attribute-domain-1', attribute_name, tbox)

    def attribute_type(self, attribute_name=None, tbox=None) -> str:
        return str(self.racer_call('attribute-type', attribute_name, tbox))

    def attribute_type_(self, attribute_name=None, tbox=None) -> RacerResult:
        return self.racer_call('attribute-type', attribute_name, tbox)

    def cd_attribute_p(self, attribute=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('cd-attribute-p', attribute, tbox))

    def cd_object_p(self, object_name=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('cd-object-p', object_name, abox))

    def cheap_queries(self, *key_args) -> str:
        return str(self.racer_call('cheap-queries', key_args))

    def cheap_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('cheap-queries', key_args)

    def cheap_query_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('cheap-query-p', query))

    def cheap_rule_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('cheap-rule-p', query))

    def cheap_rules(self, *key_args) -> str:
        return str(self.racer_call('cheap-rules', key_args))

    def cheap_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('cheap-rules', key_args)

    def check_abox_coherence(self, abox=None, filename_or_stream=None) -> str:
        return str(self.racer_call('check-abox-coherence', abox, filename_or_stream))

    def check_abox_coherence_(self, abox=None, filename_or_stream=None) -> RacerResult:
        return self.racer_call('check-abox-coherence', abox, filename_or_stream)

    def check_abox_consistency_before_querying(self) -> str:
        return str(self.racer_call('check-abox-consistency-before-querying'))

    def check_abox_consistency_before_querying_(self) -> RacerResult:
        return self.racer_call('check-abox-consistency-before-querying')

    def check_concept_coherence(self, concept=None, tbox=None) -> str:
        return str(self.racer_call('check-concept-coherence', concept, tbox))

    def check_concept_coherence_(self, concept=None, tbox=None) -> RacerResult:
        return self.racer_call('check-concept-coherence', concept, tbox)

    def check_for_updates(self, *key_args) -> str:
        return str(self.racer_call('check-for-updates', key_args))

    def check_for_updates_(self, *key_args) -> RacerResult:
        return self.racer_call('check-for-updates', key_args)

    def check_nrql_subscriptions(self, abox=None) -> str:
        return str(self.racer_call('check-nrql-subscriptions', abox))

    def check_nrql_subscriptions_(self, abox=None) -> RacerResult:
        return self.racer_call('check-nrql-subscriptions', abox)

    def check_ontology(self, *key_args) -> str:
        return str(self.racer_call('check-ontology', key_args))

    def check_ontology_(self, *key_args) -> RacerResult:
        return self.racer_call('check-ontology', key_args)

    def check_subscriptions(self, abox=None) -> str:
        return str(self.racer_call('check-subscriptions', abox))

    def check_subscriptions_(self, abox=None) -> RacerResult:
        return self.racer_call('check-subscriptions', abox)

    def check_tbox_coherence(self, *key_args) -> str:
        return str(self.racer_call('check-tbox-coherence', key_args))

    def check_tbox_coherence_(self, *key_args) -> RacerResult:
        return self.racer_call('check-tbox-coherence', key_args)

    def choose_current_set_of_rule_consequences(self, query=None) -> str:
        return str(self.racer_call('choose-current-set-of-rule-consequences', query))

    def choose_current_set_of_rule_consequences_(self, query=None) -> RacerResult:
        return self.racer_call('choose-current-set-of-rule-consequences', query)

    def classify_query(self, query=None) -> str:
        return str(self.racer_call('classify-query', query))

    def classify_query_(self, query=None) -> RacerResult:
        return self.racer_call('classify-query', query)

    def classify_tbox(self, tbox=None) -> str:
        return str(self.racer_call('classify-tbox', tbox))

    def classify_tbox_(self, tbox=None) -> RacerResult:
        return self.racer_call('classify-tbox', tbox)

    def clear_all_documentation(self) -> str:
        return str(self.racer_call('clear-all-documentation'))

    def clear_all_documentation_(self) -> RacerResult:
        return self.racer_call('clear-all-documentation')

    def clear_default_tbox(self) -> str:
        return str(self.racer_call('clear-default-tbox'))

    def clear_default_tbox_(self) -> RacerResult:
        return self.racer_call('clear-default-tbox')

    def close_triple_store(self, *key_args) -> str:
        return str(self.racer_call('close-triple-store', key_args))

    def close_triple_store_(self, *key_args) -> RacerResult:
        return self.racer_call('close-triple-store', key_args)

    def compute_abox_difference1(self, *key_args) -> str:
        return str(self.racer_call('compute-abox-difference1', key_args))

    def compute_abox_difference1_(self, *key_args) -> RacerResult:
        return self.racer_call('compute-abox-difference1', key_args)

    def compute_abox_difference2(self, *key_args) -> str:
        return str(self.racer_call('compute-abox-difference2', key_args))

    def compute_abox_difference2_(self, *key_args) -> RacerResult:
        return self.racer_call('compute-abox-difference2', key_args)

    def compute_all_implicit_role_fillers(self, abox=None) -> str:
        return str(self.racer_call('compute-all-implicit-role-fillers', abox))

    def compute_all_implicit_role_fillers_(self, abox=None) -> RacerResult:
        return self.racer_call('compute-all-implicit-role-fillers', abox)

    def compute_implicit_role_fillers(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('compute-implicit-role-fillers', individual_name, abox))

    def compute_implicit_role_fillers_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('compute-implicit-role-fillers', individual_name, abox)

    def compute_index_for_instance_retrieval(self, abox=None) -> str:
        return str(self.racer_call('compute-index-for-instance-retrieval', abox))

    def compute_index_for_instance_retrieval_(self, abox=None) -> RacerResult:
        return self.racer_call('compute-index-for-instance-retrieval', abox)

    def compute_subgraph_aboxes(self, abox_or_name=None) -> str:
        return str(self.racer_call('compute-subgraph-aboxes', abox_or_name))

    def compute_subgraph_aboxes_(self, abox_or_name=None) -> RacerResult:
        return self.racer_call('compute-subgraph-aboxes', abox_or_name)

    def concept_disjoint_p(self, concept1=None, concept2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('concept-disjoint-p', concept1, concept2, tbox))

    def concept_equivalent_p(self, concept1=None, concept2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('concept-equivalent-p', concept1, concept2, tbox))

    def concept_is_primitive_p(self, concept_name=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('concept-is-primitive-p', concept_name, tbox))

    def concept_p(self, concept_name=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('concept-p', concept_name, tbox))

    def concept_satisfiable_p(self, concept_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('concept-satisfiable-p', concept_term, tbox))

    def concept_subsumes_p(self, subsumer=None, subsumee=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('concept-subsumes-p', subsumer, subsumee, tbox))

    def constraint_entailed_p(self, constraint=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('constraint-entailed-p', constraint, abox))

    def convert_event_specs(self, in_file=None, out_file=None) -> str:
        return str(self.racer_call('convert-event-specs', in_file, out_file))

    def convert_event_specs_(self, in_file=None, out_file=None) -> RacerResult:
        return self.racer_call('convert-event-specs', in_file, out_file)

    def copy_rules(self, *key_args) -> str:
        return str(self.racer_call('copy-rules', key_args))

    def copy_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('copy-rules', key_args)

    def create_abox_clone(self, *key_args) -> str:
        return str(self.racer_call('create-abox-clone', key_args))

    def create_abox_clone_(self, *key_args) -> RacerResult:
        return self.racer_call('create-abox-clone', key_args)

    def create_data_edge(self, *key_args) -> str:
        return str(self.racer_call('create-data-edge', key_args))

    def create_data_edge_(self, *key_args) -> RacerResult:
        return self.racer_call('create-data-edge', key_args)

    def create_data_node(self, *key_args) -> str:
        return str(self.racer_call('create-data-node', key_args))

    def create_data_node_(self, *key_args) -> RacerResult:
        return self.racer_call('create-data-node', key_args)

    def create_rcc_edge(self, *key_args) -> str:
        return str(self.racer_call('create-rcc-edge', key_args))

    def create_rcc_edge_(self, *key_args) -> RacerResult:
        return self.racer_call('create-rcc-edge', key_args)

    def create_rcc_node(self, *key_args) -> str:
        return str(self.racer_call('create-rcc-node', key_args))

    def create_rcc_node_(self, *key_args) -> RacerResult:
        return self.racer_call('create-rcc-node', key_args)

    def create_subgraph_aboxes(self, abox_or_name=None, new_name=None, tbox=None) -> str:
        return str(self.racer_call('create-subgraph-aboxes', abox_or_name, new_name, tbox))

    def create_subgraph_aboxes_(self, abox_or_name=None, new_name=None, tbox=None) -> RacerResult:
        return self.racer_call('create-subgraph-aboxes', abox_or_name, new_name, tbox)

    def create_tbox_clone(self, *key_args) -> str:
        return str(self.racer_call('create-tbox-clone', key_args))

    def create_tbox_clone_(self, *key_args) -> RacerResult:
        return self.racer_call('create-tbox-clone', key_args)

    def create_tbox_internal_marker_concept(self, tbox=None, marker_name=None) -> str:
        return str(self.racer_call('create-tbox-internal-marker-concept', tbox, marker_name))

    def create_tbox_internal_marker_concept_(self, tbox=None, marker_name=None) -> RacerResult:
        return self.racer_call('create-tbox-internal-marker-concept', tbox, marker_name)

    def create_triple_store(self, *key_args) -> str:
        return str(self.racer_call('create-triple-store', key_args))

    def create_triple_store_(self, *key_args) -> RacerResult:
        return self.racer_call('create-triple-store', key_args)

    def current_abox(self) -> str:
        return str(self.racer_call('current-abox'))

    def current_abox_(self) -> RacerResult:
        return self.racer_call('current-abox')

    def current_tbox(self) -> str:
        return str(self.racer_call('current-tbox'))

    def current_tbox_(self) -> RacerResult:
        return self.racer_call('current-tbox')

    def data_edge1(self, from_=None, to=None, data_relation=None, racer_descr=None, abox=None) -> str:
        return str(self.racer_call('data-edge1', from_, to, data_relation, racer_descr, abox))

    def data_edge1_(self, from_=None, to=None, data_relation=None, abox=None, racer_descr=None) -> RacerResult:
        return self.racer_call('data-edge1', from_, to, data_relation, abox, racer_descr)

    def data_node1(self, name=None, descr=None, racer_descr=None, abox=None) -> str:
        return str(self.racer_call('data-node1', name, descr, racer_descr, abox))

    def data_node1_(self, name=None, descr=None, racer_descr=None, abox=None) -> RacerResult:
        return self.racer_call('data-node1', name, descr, racer_descr, abox)

    def datatype_role_has_range(self, rolename=None, range=None, tbox=None) -> str:
        return str(self.racer_call('datatype-role-has-range', rolename, range, tbox))

    def datatype_role_has_range_(self, rolename=None, range=None, tbox=None) -> RacerResult:
        return self.racer_call('datatype-role-has-range', rolename, range, tbox)

    def datatype_role_range(self, role_name=None, tbox=None) -> str:
        return str(self.racer_call('datatype-role-range', role_name, tbox))

    def datatype_role_range_(self, role_name=None, tbox=None) -> RacerResult:
        return self.racer_call('datatype-role-range', role_name, tbox)

    def deactivate_defined_query(self, *key_args) -> str:
        return str(self.racer_call('deactivate-defined-query', key_args))

    def deactivate_defined_query_(self, *key_args) -> RacerResult:
        return self.racer_call('deactivate-defined-query', key_args)

    def declare_current_knowledge_bases_as_persistent(self) -> str:
        return str(self.racer_call('declare-current-knowledge-bases-as-persistent'))

    def declare_current_knowledge_bases_as_persistent_(self) -> RacerResult:
        return self.racer_call('declare-current-knowledge-bases-as-persistent')

    def declare_disjoint(self, concepts=None, tbox=None) -> str:
        return str(self.racer_call('declare-disjoint', concepts, tbox))

    def declare_disjoint_(self, concepts=None, tbox=None) -> RacerResult:
        return self.racer_call('declare-disjoint', concepts, tbox)

    def defcon1(self, name=None, value=None) -> str:
        return str(self.racer_call('defcon1', name, value))

    def defcon1_(self, name=None, value=None) -> RacerResult:
        return self.racer_call('defcon1', name, value)

    def define_and_execute_query(self, *key_args) -> str:
        return str(self.racer_call('define-and-execute-query', key_args))

    def define_and_execute_query_(self, *key_args) -> RacerResult:
        return self.racer_call('define-and-execute-query', key_args)

    def define_and_prepare_query(self, *key_args) -> str:
        return str(self.racer_call('define-and-prepare-query', key_args))

    def define_and_prepare_query_(self, *key_args) -> RacerResult:
        return self.racer_call('define-and-prepare-query', key_args)

    def define_query(self, *key_args) -> str:
        return str(self.racer_call('define-query', key_args))

    def define_query_(self, *key_args) -> RacerResult:
        return self.racer_call('define-query', key_args)

    def define1(self, name=None, arglist=None) -> str:
        return str(self.racer_call('define1', name, arglist))

    def define1_(self, name=None, arglist=None) -> RacerResult:
        return self.racer_call('define1', name, arglist)

    def defpar1(self, name=None, value=None) -> str:
        return str(self.racer_call('defpar1', name, value))

    def defpar1_(self, name=None, value=None) -> RacerResult:
        return self.racer_call('defpar1', name, value)

    def del_data_edge1(self, from_=None, to=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('del-data-edge1', from_, to, abox, type_of_substrate))

    def del_data_edge1_(self, from_=None, to=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('del-data-edge1', from_, to, abox, type_of_substrate)

    def del_data_node1(self, name=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('del-data-node1', name, abox, type_of_substrate))

    def del_data_node1_(self, name=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('del-data-node1', name, abox, type_of_substrate)

    def del_doc_entry1(self, label=None) -> str:
        return str(self.racer_call('del-doc-entry1', label))

    def del_doc_entry1_(self, label=None) -> RacerResult:
        return self.racer_call('del-doc-entry1', label)

    def del_rcc_edge1(self) -> str:
        return str(self.racer_call('del-rcc-edge1'))

    def del_rcc_edge1_(self) -> RacerResult:
        return self.racer_call('del-rcc-edge1')

    def del_rcc_node1(self) -> str:
        return str(self.racer_call('del-rcc-node1'))

    def del_rcc_node1_(self) -> RacerResult:
        return self.racer_call('del-rcc-node1')

    def delete_all_aboxes(self) -> str:
        return str(self.racer_call('delete-all-aboxes'))

    def delete_all_aboxes_(self) -> RacerResult:
        return self.racer_call('delete-all-aboxes')

    def delete_all_definitions(self, *key_args) -> str:
        return str(self.racer_call('delete-all-definitions', key_args))

    def delete_all_definitions_(self, *key_args) -> RacerResult:
        return self.racer_call('delete-all-definitions', key_args)

    def delete_all_queries(self, *key_args) -> str:
        return str(self.racer_call('delete-all-queries', key_args))

    def delete_all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('delete-all-queries', key_args)

    def delete_all_rules(self, *key_args) -> str:
        return str(self.racer_call('delete-all-rules', key_args))

    def delete_all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('delete-all-rules', key_args)

    def delete_all_substrates(self, *key_args) -> str:
        return str(self.racer_call('delete-all-substrates', key_args))

    def delete_all_substrates_(self, *key_args) -> RacerResult:
        return self.racer_call('delete-all-substrates', key_args)

    def delete_all_tboxes(self) -> str:
        return str(self.racer_call('delete-all-tboxes'))

    def delete_all_tboxes_(self) -> RacerResult:
        return self.racer_call('delete-all-tboxes')

    def delete_data_edge(self, *key_args) -> str:
        return str(self.racer_call('delete-data-edge', key_args))

    def delete_data_edge_(self, *key_args) -> RacerResult:
        return self.racer_call('delete-data-edge', key_args)

    def delete_data_node(self, *key_args) -> str:
        return str(self.racer_call('delete-data-node', key_args))

    def delete_data_node_(self, *key_args) -> RacerResult:
        return self.racer_call('delete-data-node', key_args)

    def delete_prefix_mappings(self) -> str:
        return str(self.racer_call('delete-prefix-mappings'))

    def delete_prefix_mappings_(self) -> RacerResult:
        return self.racer_call('delete-prefix-mappings')

    def delete_query(self, query=None) -> str:
        return str(self.racer_call('delete-query', query))

    def delete_query_(self, query=None) -> RacerResult:
        return self.racer_call('delete-query', query)

    def delete_rcc_synonyms(self) -> str:
        return str(self.racer_call('delete-rcc-synonyms'))

    def delete_rcc_synonyms_(self) -> RacerResult:
        return self.racer_call('delete-rcc-synonyms')

    def delete_rule(self, query=None) -> str:
        return str(self.racer_call('delete-rule', query))

    def delete_rule_(self, query=None) -> RacerResult:
        return self.racer_call('delete-rule', query)

    def describe_abox(self, abox=None, stream=None) -> str:
        return str(self.racer_call('describe-abox', abox, stream))

    def describe_abox_(self, abox=None, stream=None) -> RacerResult:
        return self.racer_call('describe-abox', abox, stream)

    def describe_all_definitions(self, *key_args) -> str:
        return str(self.racer_call('describe-all-definitions', key_args))

    def describe_all_definitions_(self, *key_args) -> RacerResult:
        return self.racer_call('describe-all-definitions', key_args)

    def describe_all_edges(self, *key_args) -> str:
        return str(self.racer_call('describe-all-edges', key_args))

    def describe_all_edges_(self, *key_args) -> RacerResult:
        return self.racer_call('describe-all-edges', key_args)

    def describe_all_nodes(self, *key_args) -> str:
        return str(self.racer_call('describe-all-nodes', key_args))

    def describe_all_nodes_(self, *key_args) -> RacerResult:
        return self.racer_call('describe-all-nodes', key_args)

    def describe_all_queries(self, *key_args) -> str:
        return str(self.racer_call('describe-all-queries', key_args))

    def describe_all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('describe-all-queries', key_args)

    def describe_all_rules(self, *key_args) -> str:
        return str(self.racer_call('describe-all-rules', key_args))

    def describe_all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('describe-all-rules', key_args)

    def describe_all_substrates(self) -> str:
        return str(self.racer_call('describe-all-substrates'))

    def describe_all_substrates_(self) -> RacerResult:
        return self.racer_call('describe-all-substrates')

    def describe_concept(self, concept_name=None, tbox=None, stream=None) -> str:
        return str(self.racer_call('describe-concept', concept_name, tbox, stream))

    def describe_concept_(self, concept_name=None, tbox=None, stream=None) -> RacerResult:
        return self.racer_call('describe-concept', concept_name, tbox, stream)

    def describe_current_substrate(self) -> str:
        return str(self.racer_call('describe-current-substrate'))

    def describe_current_substrate_(self) -> RacerResult:
        return self.racer_call('describe-current-substrate')

    def describe_definition(self, *key_args) -> str:
        return str(self.racer_call('describe-definition', key_args))

    def describe_definition_(self, *key_args) -> RacerResult:
        return self.racer_call('describe-definition', key_args)

    def describe_individual(self, individual_name=None, abox=None, stream=None) -> str:
        return str(self.racer_call('describe-individual', individual_name, abox, stream))

    def describe_individual_(self, individual_name=None, abox=None, stream=None) -> RacerResult:
        return self.racer_call('describe-individual', individual_name, abox, stream)

    def describe_individual1(self, individual_name=None, abox=None, stream=None) -> str:
        return str(self.racer_call('describe-individual1', individual_name, abox, stream))

    def describe_individual1_(self, individual_name=None, abox=None, stream=None) -> RacerResult:
        return self.racer_call('describe-individual1', individual_name, abox, stream)

    def describe_query(self, query=None, rewritten_p=None) -> str:
        return str(self.racer_call('describe-query', query, rewritten_p))

    def describe_query_(self, query=None, rewritten_p=None) -> RacerResult:
        return self.racer_call('describe-query', query, rewritten_p)

    def describe_query_processing_mode(self) -> str:
        return str(self.racer_call('describe-query-processing-mode'))

    def describe_query_processing_mode_(self) -> RacerResult:
        return self.racer_call('describe-query-processing-mode')

    def describe_query_status(self, query=None) -> str:
        return str(self.racer_call('describe-query-status', query))

    def describe_query_status_(self, query=None) -> RacerResult:
        return self.racer_call('describe-query-status', query)

    def describe_role(self, role_term=None, tbox=None, stream=None) -> str:
        return str(self.racer_call('describe-role', role_term, tbox, stream))

    def describe_role_(self, role_term=None, tbox=None, stream=None) -> RacerResult:
        return self.racer_call('describe-role', role_term, tbox, stream)

    def describe_rule(self, query=None, rewritten_p=None) -> str:
        return str(self.racer_call('describe-rule', query, rewritten_p))

    def describe_rule_(self, query=None, rewritten_p=None) -> RacerResult:
        return self.racer_call('describe-rule', query, rewritten_p)

    def describe_rule_status(self, query=None) -> str:
        return str(self.racer_call('describe-rule-status', query))

    def describe_rule_status_(self, query=None) -> RacerResult:
        return self.racer_call('describe-rule-status', query)

    def describe_substrate(self, *key_args) -> str:
        return str(self.racer_call('describe-substrate', key_args))

    def describe_substrate_(self, *key_args) -> RacerResult:
        return self.racer_call('describe-substrate', key_args)

    def describe_tbox(self, tbox=None, stream=None) -> str:
        return str(self.racer_call('describe-tbox', tbox, stream))

    def describe_tbox_(self, tbox=None, stream=None) -> RacerResult:
        return self.racer_call('describe-tbox', tbox, stream)

    def description_implies_p(self, a=None, b=None) -> bool:
        return self.return_boolean(self.racer_call('description-implies-p', a, b))

    def dig_read_document(self, url_spec=None, kb_name=None, init=None) -> str:
        return str(self.racer_call('dig-read-document', url_spec, kb_name, init))

    def dig_read_document_(self, url_spec=None, kb_name=None, init=None) -> RacerResult:
        return self.racer_call('dig-read-document', url_spec, kb_name, init)

    def dig_read_file(self, *key_args) -> str:
        return str(self.racer_call('dig-read-file', key_args))

    def dig_read_file_(self, *key_args) -> RacerResult:
        return self.racer_call('dig-read-file', key_args)

    def disable_abduction(self, *key_args) -> str:
        return str(self.racer_call('disable-abduction', key_args))

    def disable_abduction_(self, *key_args) -> RacerResult:
        return self.racer_call('disable-abduction', key_args)

    def disable_abox_mirroring(self) -> str:
        return str(self.racer_call('disable-abox-mirroring'))

    def disable_abox_mirroring_(self) -> RacerResult:
        return self.racer_call('disable-abox-mirroring')

    def disable_data_substrate_mirroring(self) -> str:
        return str(self.racer_call('disable-data-substrate-mirroring'))

    def disable_data_substrate_mirroring_(self) -> RacerResult:
        return self.racer_call('disable-data-substrate-mirroring')

    def disable_defined_queries(self) -> str:
        return str(self.racer_call('disable-defined-queries'))

    def disable_defined_queries_(self) -> RacerResult:
        return self.racer_call('disable-defined-queries')

    def disable_kb_has_changed_warning_tokens(self) -> str:
        return str(self.racer_call('disable-kb-has-changed-warning-tokens'))

    def disable_kb_has_changed_warning_tokens_(self) -> RacerResult:
        return self.racer_call('disable-kb-has-changed-warning-tokens')

    def disable_lazy_unfolding_of_defined_queries(self) -> str:
        return str(self.racer_call('disable-lazy-unfolding-of-defined-queries'))

    def disable_lazy_unfolding_of_defined_queries_(self) -> RacerResult:
        return self.racer_call('disable-lazy-unfolding-of-defined-queries')

    def disable_nrql_warnings(self) -> str:
        return str(self.racer_call('disable-nrql-warnings'))

    def disable_nrql_warnings_(self) -> RacerResult:
        return self.racer_call('disable-nrql-warnings')

    def disable_phase_two_starts_warning_tokens(self) -> str:
        return str(self.racer_call('disable-phase-two-starts-warning-tokens'))

    def disable_phase_two_starts_warning_tokens_(self) -> RacerResult:
        return self.racer_call('disable-phase-two-starts-warning-tokens')

    def disable_query_optimization(self) -> str:
        return str(self.racer_call('disable-query-optimization'))

    def disable_query_optimization_(self) -> RacerResult:
        return self.racer_call('disable-query-optimization')

    def disable_query_realization(self) -> str:
        return str(self.racer_call('disable-query-realization'))

    def disable_query_realization_(self) -> RacerResult:
        return self.racer_call('disable-query-realization')

    def disable_query_repository(self) -> str:
        return str(self.racer_call('disable-query-repository'))

    def disable_query_repository_(self) -> RacerResult:
        return self.racer_call('disable-query-repository')

    def disable_rcc_substrate_mirroring(self) -> str:
        return str(self.racer_call('disable-rcc-substrate-mirroring'))

    def disable_rcc_substrate_mirroring_(self) -> RacerResult:
        return self.racer_call('disable-rcc-substrate-mirroring')

    def disable_told_information_querying(self) -> str:
        return str(self.racer_call('disable-told-information-querying'))

    def disable_told_information_querying_(self) -> RacerResult:
        return self.racer_call('disable-told-information-querying')

    def disable_two_phase_query_processing_mode(self) -> str:
        return str(self.racer_call('disable-two-phase-query-processing-mode'))

    def disable_two_phase_query_processing_mode_(self) -> RacerResult:
        return self.racer_call('disable-two-phase-query-processing-mode')

    def dont_add_missing_top_conjuncts(self) -> str:
        return str(self.racer_call('dont-add-missing-top-conjuncts'))

    def dont_add_missing_top_conjuncts_(self) -> RacerResult:
        return self.racer_call('dont-add-missing-top-conjuncts')

    def dont_add_role_assertions_for_datatype_properties(self) -> str:
        return str(self.racer_call('dont-add-role-assertions-for-datatype-properties'))

    def dont_add_role_assertions_for_datatype_properties_(self) -> RacerResult:
        return self.racer_call('dont-add-role-assertions-for-datatype-properties')

    def dont_add_rule_consequences_automatically(self) -> str:
        return str(self.racer_call('dont-add-rule-consequences-automatically'))

    def dont_add_rule_consequences_automatically_(self) -> RacerResult:
        return self.racer_call('dont-add-rule-consequences-automatically')

    def dont_allow_overloaded_definitions(self) -> str:
        return str(self.racer_call('dont-allow-overloaded-definitions'))

    def dont_allow_overloaded_definitions_(self) -> RacerResult:
        return self.racer_call('dont-allow-overloaded-definitions')

    def dont_check_abox_consistency_before_querying(self) -> str:
        return str(self.racer_call('dont-check-abox-consistency-before-querying'))

    def dont_check_abox_consistency_before_querying_(self) -> RacerResult:
        return self.racer_call('dont-check-abox-consistency-before-querying')

    def dont_keep_defined_query_atoms(self) -> str:
        return str(self.racer_call('dont-keep-defined-query-atoms'))

    def dont_keep_defined_query_atoms_(self) -> RacerResult:
        return self.racer_call('dont-keep-defined-query-atoms')

    def dont_prefer_defined_queries(self) -> str:
        return str(self.racer_call('dont-prefer-defined-queries'))

    def dont_prefer_defined_queries_(self) -> RacerResult:
        return self.racer_call('dont-prefer-defined-queries')

    def dont_report_inconsistent_queries_and_rules(self) -> str:
        return str(self.racer_call('dont-report-inconsistent-queries-and-rules'))

    def dont_report_inconsistent_queries_and_rules_(self) -> RacerResult:
        return self.racer_call('dont-report-inconsistent-queries-and-rules')

    def dont_use_individual_synonym_equivalence_classes(self) -> str:
        return str(self.racer_call('dont-use-individual-synonym-equivalence-classes'))

    def dont_use_individual_synonym_equivalence_classes_(self) -> RacerResult:
        return self.racer_call('dont-use-individual-synonym-equivalence-classes')

    def dont_use_injective_variables_by_default(self) -> str:
        return str(self.racer_call('dont-use-injective-variables-by-default'))

    def dont_use_injective_variables_by_default_(self) -> RacerResult:
        return self.racer_call('dont-use-injective-variables-by-default')

    def edge_description1(self, from_=None, to=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('edge-description1', from_, to, abox, type_of_substrate))

    def edge_description1_(self, from_=None, to=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('edge-description1', from_, to, abox, type_of_substrate)

    def edge_label1(self, from_=None, to=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('edge-label1', from_, to, abox, type_of_substrate))

    def edge_label1_(self, from_=None, to=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('edge-label1', from_, to, abox, type_of_substrate)

    def enable_abduction(self, *key_args) -> str:
        return str(self.racer_call('enable-abduction', key_args))

    def enable_abduction_(self, *key_args) -> RacerResult:
        return self.racer_call('enable-abduction', key_args)

    def enable_abox_mirroring(self) -> str:
        return str(self.racer_call('enable-abox-mirroring'))

    def enable_abox_mirroring_(self) -> RacerResult:
        return self.racer_call('enable-abox-mirroring')

    def enable_data_substrate_mirroring(self) -> str:
        return str(self.racer_call('enable-data-substrate-mirroring'))

    def enable_data_substrate_mirroring_(self) -> RacerResult:
        return self.racer_call('enable-data-substrate-mirroring')

    def enable_defined_queries(self) -> str:
        return str(self.racer_call('enable-defined-queries'))

    def enable_defined_queries_(self) -> RacerResult:
        return self.racer_call('enable-defined-queries')

    def enable_eager_tuple_computation(self) -> str:
        return str(self.racer_call('enable-eager-tuple-computation'))

    def enable_eager_tuple_computation_(self) -> RacerResult:
        return self.racer_call('enable-eager-tuple-computation')

    def enable_kb_has_changed_warning_tokens(self) -> str:
        return str(self.racer_call('enable-kb-has-changed-warning-tokens'))

    def enable_kb_has_changed_warning_tokens_(self) -> RacerResult:
        return self.racer_call('enable-kb-has-changed-warning-tokens')

    def enable_lazy_tuple_computation(self) -> str:
        return str(self.racer_call('enable-lazy-tuple-computation'))

    def enable_lazy_tuple_computation_(self) -> RacerResult:
        return self.racer_call('enable-lazy-tuple-computation')

    def enable_lazy_unfolding_of_defined_queries(self) -> str:
        return str(self.racer_call('enable-lazy-unfolding-of-defined-queries'))

    def enable_lazy_unfolding_of_defined_queries_(self) -> RacerResult:
        return self.racer_call('enable-lazy-unfolding-of-defined-queries')

    def enable_nrql_warnings(self) -> str:
        return str(self.racer_call('enable-nrql-warnings'))

    def enable_nrql_warnings_(self) -> RacerResult:
        return self.racer_call('enable-nrql-warnings')

    def enable_optimized_query_processing(self, rewrite_concept_definitions=None) -> str:
        return str(self.racer_call('enable-optimized-query-processing', rewrite_concept_definitions))

    def enable_optimized_query_processing_(self, rewrite_concept_definitions=None) -> RacerResult:
        return self.racer_call('enable-optimized-query-processing', rewrite_concept_definitions)

    def enable_phase_two_starts_warning_tokens(self) -> str:
        return str(self.racer_call('enable-phase-two-starts-warning-tokens'))

    def enable_phase_two_starts_warning_tokens_(self) -> RacerResult:
        return self.racer_call('enable-phase-two-starts-warning-tokens')

    def enable_query_optimization(self) -> str:
        return str(self.racer_call('enable-query-optimization'))

    def enable_query_optimization_(self) -> RacerResult:
        return self.racer_call('enable-query-optimization')

    def enable_query_realization(self) -> str:
        return str(self.racer_call('enable-query-realization'))

    def enable_query_realization_(self) -> RacerResult:
        return self.racer_call('enable-query-realization')

    def enable_query_repository(self) -> str:
        return str(self.racer_call('enable-query-repository'))

    def enable_query_repository_(self) -> RacerResult:
        return self.racer_call('enable-query-repository')

    def enable_rcc_substrate_mirroring(self) -> str:
        return str(self.racer_call('enable-rcc-substrate-mirroring'))

    def enable_rcc_substrate_mirroring_(self) -> RacerResult:
        return self.racer_call('enable-rcc-substrate-mirroring')

    def enable_smart_abox_mirroring(self) -> str:
        return str(self.racer_call('enable-smart-abox-mirroring'))

    def enable_smart_abox_mirroring_(self) -> RacerResult:
        return self.racer_call('enable-smart-abox-mirroring')

    def enable_told_information_querying(self) -> str:
        return str(self.racer_call('enable-told-information-querying'))

    def enable_told_information_querying_(self) -> RacerResult:
        return self.racer_call('enable-told-information-querying')

    def enable_two_phase_query_processing_mode(self) -> str:
        return str(self.racer_call('enable-two-phase-query-processing-mode'))

    def enable_two_phase_query_processing_mode_(self) -> RacerResult:
        return self.racer_call('enable-two-phase-query-processing-mode')

    def enable_very_smart_abox_mirroring(self) -> str:
        return str(self.racer_call('enable-very-smart-abox-mirroring'))

    def enable_very_smart_abox_mirroring_(self) -> RacerResult:
        return self.racer_call('enable-very-smart-abox-mirroring')

    def ensure_abox_signature(self, *key_args) -> str:
        return str(self.racer_call('ensure-abox-signature', key_args))

    def ensure_abox_signature_(self, *key_args) -> RacerResult:
        return self.racer_call('ensure-abox-signature', key_args)

    def ensure_subsumption_based_query_answering(self, abox=None) -> str:
        return str(self.racer_call('ensure-subsumption-based-query-answering', abox))

    def ensure_subsumption_based_query_answering_(self, abox=None) -> RacerResult:
        return self.racer_call('ensure-subsumption-based-query-answering', abox)

    def ensure_tbox_signature(self, *key_args) -> str:
        return str(self.racer_call('ensure-tbox-signature', key_args))

    def ensure_tbox_signature_(self, *key_args) -> RacerResult:
        return self.racer_call('ensure-tbox-signature', key_args)

    def exclude_permutations(self) -> str:
        return str(self.racer_call('exclude-permutations'))

    def exclude_permutations_(self) -> RacerResult:
        return self.racer_call('exclude-permutations')

    def execute_all_queries(self, *key_args) -> str:
        return str(self.racer_call('execute-all-queries', key_args))

    def execute_all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('execute-all-queries', key_args)

    def execute_all_rules(self, *key_args) -> str:
        return str(self.racer_call('execute-all-rules', key_args))

    def execute_all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('execute-all-rules', key_args)

    def execute_applicable_rules(self, *key_args) -> str:
        return str(self.racer_call('execute-applicable-rules', key_args))

    def execute_applicable_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('execute-applicable-rules', key_args)

    def execute_or_reexecute_all_queries(self, *key_args) -> str:
        return str(self.racer_call('execute-or-reexecute-all-queries', key_args))

    def execute_or_reexecute_all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('execute-or-reexecute-all-queries', key_args)

    def execute_or_reexecute_all_rules(self, *key_args) -> str:
        return str(self.racer_call('execute-or-reexecute-all-rules', key_args))

    def execute_or_reexecute_all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('execute-or-reexecute-all-rules', key_args)

    def execute_or_reexecute_query(self, *key_args) -> str:
        return str(self.racer_call('execute-or-reexecute-query', key_args))

    def execute_or_reexecute_query_(self, *key_args) -> RacerResult:
        return self.racer_call('execute-or-reexecute-query', key_args)

    def execute_or_reexecute_rule(self, query=None) -> str:
        return str(self.racer_call('execute-or-reexecute-rule', query))

    def execute_or_reexecute_rule_(self, query=None) -> RacerResult:
        return self.racer_call('execute-or-reexecute-rule', query)

    def execute_query(self, *key_args) -> str:
        return str(self.racer_call('execute-query', key_args))

    def execute_query_(self, *key_args) -> RacerResult:
        return self.racer_call('execute-query', key_args)

    def execute_rule(self, query=None) -> str:
        return str(self.racer_call('execute-rule', query))

    def execute_rule_(self, query=None) -> RacerResult:
        return self.racer_call('execute-rule', query)

    def expensive_queries(self, *key_args) -> str:
        return str(self.racer_call('expensive-queries', key_args))

    def expensive_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('expensive-queries', key_args)

    def expensive_query_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('expensive-query-p', query))

    def expensive_rule_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('expensive-rule-p', query))

    def expensive_rules(self, *key_args) -> str:
        return str(self.racer_call('expensive-rules', key_args))

    def expensive_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('expensive-rules', key_args)

    def fcall(self, name=None) -> str:
        return str(self.racer_call('fcall', name))

    def fcall_(self, name=None) -> RacerResult:
        return self.racer_call('fcall', name)

    def feature_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('feature-p', role_term, tbox))

    def find_abox(self, abox_name_or_abox=None, errorp=None) -> str:
        return str(self.racer_call('find-abox', abox_name_or_abox, errorp))

    def find_abox_(self, abox_name_or_abox=None, errorp=None) -> RacerResult:
        return self.racer_call('find-abox', abox_name_or_abox, errorp)

    def find_tbox(self, tbox=None, errorp=None) -> str:
        return str(self.racer_call('find-tbox', tbox, errorp))

    def find_tbox_(self, tbox=None, errorp=None) -> RacerResult:
        return self.racer_call('find-tbox', tbox, errorp)

    def forget_abox(self, abox=None) -> str:
        return str(self.racer_call('forget-abox', abox))

    def forget_abox_(self, abox=None) -> RacerResult:
        return self.racer_call('forget-abox', abox)

    def forget_all_different_assertion(self, abox=None, individual_name_set=None) -> str:
        return str(self.racer_call('forget-all-different-assertion', abox, individual_name_set))

    def forget_all_different_assertion_(self, abox=None, individual_name_set=None) -> RacerResult:
        return self.racer_call('forget-all-different-assertion', abox, individual_name_set)

    def forget_annotation_concept_assertion(self, abox=None, individual_name=None, concept=None) -> str:
        return str(self.racer_call('forget-annotation-concept-assertion', abox, individual_name, concept))

    def forget_annotation_concept_assertion_(self, abox=None, individual_name=None,
                                             concept=None) -> RacerResult:
        return self.racer_call('forget-annotation-concept-assertion', abox, individual_name, concept)

    def forget_concept_assertion(self, abox=None, individual_name=None, concept=None) -> str:
        return str(self.racer_call('forget-concept-assertion', abox, individual_name, concept))

    def forget_concept_assertion_(self, abox=None, individual_name=None, concept=None) -> RacerResult:
        return self.racer_call('forget-concept-assertion', abox, individual_name, concept)

    def forget_concept_axiom(self, *key_args) -> str:
        return str(self.racer_call('forget-concept-axiom', key_args))

    def forget_concept_axiom_(self, *key_args) -> RacerResult:
        return self.racer_call('forget-concept-axiom', key_args)

    def forget_constrained_assertion(self, abox=None, individual_name=None, object_name=None,
                                     attribute_term=None) -> str:
        return str(self.racer_call('forget-constrained-assertion', abox, individual_name, object_name, attribute_term))

    def forget_constrained_assertion_(self, abox=None, individual_name=None, object_name=None,
                                      attribute_term=None) -> RacerResult:
        return self.racer_call('forget-constrained-assertion', abox, individual_name, object_name, attribute_term)

    def forget_constraint(self, abox=None, constraint=None) -> str:
        return str(self.racer_call('forget-constraint', abox, constraint))

    def forget_constraint_(self, abox=None, constraint=None) -> RacerResult:
        return self.racer_call('forget-constraint', abox, constraint)

    def forget_datatype_role_filler(self, abox=None, individual=None, value=None, role=None) -> str:
        return str(self.racer_call('forget-datatype-role-filler', abox, individual, value, role))

    def forget_datatype_role_filler_(self, abox=None, individual=None, value=None,
                                     role=None) -> RacerResult:
        return self.racer_call('forget-datatype-role-filler', abox, individual, value, role)

    def forget_different_from_assertion(self, abox=None, individual1=None, individual2=None) -> str:
        return str(self.racer_call('forget-different-from-assertion', abox, individual1, individual2))

    def forget_different_from_assertion_(self, abox=None, individual1=None, individual2=None) -> RacerResult:
        return self.racer_call('forget-different-from-assertion', abox, individual1, individual2)

    def forget_disjointness_axiom(self, tbox=None, concept_name=None, group_name=None, form=None) -> str:
        return str(self.racer_call('forget-disjointness-axiom', tbox, concept_name, group_name, form))

    def forget_disjointness_axiom_(self, tbox=None, concept_name=None, group_name=None) -> RacerResult:
        return self.racer_call('forget-disjointness-axiom', tbox, concept_name, group_name)

    def forget_disjointness_axiom_statement(self, tbox=None, concepts=None) -> str:
        return str(self.racer_call('forget-disjointness-axiom-statement', tbox, concepts))

    def forget_disjointness_axiom_statement_(self, tbox=None, concepts=None) -> RacerResult:
        return self.racer_call('forget-disjointness-axiom-statement', tbox, concepts)

    def forget_individual(self, individual=None, abox=None) -> str:
        return str(self.racer_call('forget-individual', individual, abox))

    def forget_individual_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('forget-individual', individual, abox)

    def forget_negated_role_assertion(self, abox=None, predecessor_name=None, filler_name=None,
                                      role_term=None) -> str:
        return str(self.racer_call('forget-negated-role-assertion', abox, predecessor_name, filler_name, role_term))

    def forget_negated_role_assertion_(self, abox=None, predecessor_name=None, filler_name=None,
                                       role_term=None) -> RacerResult:
        return self.racer_call('forget-negated-role-assertion', abox, predecessor_name, filler_name, role_term)

    def forget_negative_datatype_role_filler(self, abox=None, individual=None, value=None,
                                             role=None) -> str:
        return str(self.racer_call('forget-negative-datatype-role-filler', abox, individual, value, role))

    def forget_negative_datatype_role_filler_(self, abox=None, individual=None, value=None,
                                              role=None) -> RacerResult:
        return self.racer_call('forget-negative-datatype-role-filler', abox, individual, value, role)

    def forget_role_assertion(self, abox=None, predecessor_name=None, filler_name=None,
                              role_term=None) -> str:
        return str(self.racer_call('forget-role-assertion', abox, predecessor_name, filler_name, role_term))

    def forget_role_assertion_(self, abox=None, predecessor_name=None, filler_name=None,
                               role_term=None) -> RacerResult:
        return self.racer_call('forget-role-assertion', abox, predecessor_name, filler_name, role_term)

    def forget_role_axioms(self, *key_args) -> str:
        return str(self.racer_call('forget-role-axioms', key_args))

    def forget_role_axioms_(self, *key_args) -> RacerResult:
        return self.racer_call('forget-role-axioms', key_args)

    def forget_same_individual_as_assertion(self, abox=None, individual1=None, individual2=None) -> str:
        return str(self.racer_call('forget-same-individual-as-assertion', abox, individual1, individual2))

    def forget_same_individual_as_assertion_(self, abox=None, individual1=None,
                                             individual2=None) -> RacerResult:
        return self.racer_call('forget-same-individual-as-assertion', abox, individual1, individual2)

    def forget_statement(self, tbox=None, abox=None, assertions=None) -> str:
        return str(self.racer_call('forget-statement', tbox, abox, assertions))

    def forget_statement_(self, tbox=None, abox=None, assertions=None) -> RacerResult:
        return self.racer_call('forget-statement', tbox, abox, assertions)

    def forget_tbox(self, tbox=None) -> str:
        return str(self.racer_call('forget-tbox', tbox))

    def forget_tbox_(self, tbox=None) -> RacerResult:
        return self.racer_call('forget-tbox', tbox)

    def full_reset(self) -> str:
        return str(self.racer_call('full-reset'))

    def full_reset_(self) -> RacerResult:
        return self.racer_call('full-reset')

    def get_abox_graph(self, *key_args) -> str:
        return str(self.racer_call('get-abox-graph', key_args))

    def get_abox_graph_(self, *key_args) -> RacerResult:
        return self.racer_call('get-abox-graph', key_args)

    def get_abox_language(self, abox=None) -> str:
        return str(self.racer_call('get-abox-language', abox))

    def get_abox_language_(self, abox=None) -> RacerResult:
        return self.racer_call('get-abox-language', abox)

    def get_abox_signature(self, abox=None) -> str:
        return str(self.racer_call('get-abox-signature', abox))

    def get_abox_signature_(self, abox=None) -> RacerResult:
        return self.racer_call('get-abox-signature', abox)

    def get_abox_version(self, abox=None) -> str:
        return str(self.racer_call('get-abox-version', abox))

    def get_abox_version_(self, abox=None) -> RacerResult:
        return self.racer_call('get-abox-version', abox)

    def get_agraph_version(self) -> str:
        return str(self.racer_call('get-agraph-version'))

    def get_agraph_version_(self) -> RacerResult:
        return self.racer_call('get-agraph-version')

    def get_all_answers(self, *key_args) -> str:
        return str(self.racer_call('get-all-answers', key_args))

    def get_all_answers_(self, *key_args) -> RacerResult:
        return self.racer_call('get-all-answers', key_args)

    def get_all_functions(self) -> str:
        return str(self.racer_call('get-all-functions'))

    def get_all_functions_(self) -> RacerResult:
        return self.racer_call('get-all-functions')

    def get_all_remaining_sets_of_rule_consequences(self, query=None) -> str:
        return str(self.racer_call('get-all-remaining-sets-of-rule-consequences', query))

    def get_all_remaining_sets_of_rule_consequences_(self, query=None) -> RacerResult:
        return self.racer_call('get-all-remaining-sets-of-rule-consequences', query)

    def get_all_remaining_tuples(self, *key_args) -> str:
        return str(self.racer_call('get-all-remaining-tuples', key_args))

    def get_all_remaining_tuples_(self, *key_args) -> RacerResult:
        return self.racer_call('get-all-remaining-tuples', key_args)

    def get_all_server_functions(self) -> str:
        return str(self.racer_call('get-all-server-functions'))

    def get_all_server_functions_(self) -> RacerResult:
        return self.racer_call('get-all-server-functions')

    def get_all_server_values(self) -> str:
        return str(self.racer_call('get-all-server-values'))

    def get_all_server_values_(self) -> RacerResult:
        return self.racer_call('get-all-server-values')

    def get_all_values(self) -> str:
        return str(self.racer_call('get-all-values'))

    def get_all_values_(self) -> RacerResult:
        return self.racer_call('get-all-values')

    def get_answer(self, *key_args) -> str:
        return str(self.racer_call('get-answer', key_args))

    def get_answer_(self, *key_args) -> RacerResult:
        return self.racer_call('get-answer', key_args)

    def get_answer_size(self, *key_args) -> str:
        return str(self.racer_call('get-answer-size', key_args))

    def get_answer_size_(self, *key_args) -> RacerResult:
        return self.racer_call('get-answer-size', key_args)

    def get_build_version(self) -> str:
        return str(self.racer_call('get-build-version'))

    def get_build_version_(self) -> RacerResult:
        return self.racer_call('get-build-version')

    def get_chosen_sets_of_rule_consequences(self, query=None) -> str:
        return str(self.racer_call('get-chosen-sets-of-rule-consequences', query))

    def get_chosen_sets_of_rule_consequences_(self, query=None) -> RacerResult:
        return self.racer_call('get-chosen-sets-of-rule-consequences', query)

    def get_concept_definition1(self, concept_name=None, tbox=None) -> str:
        return str(self.racer_call('get-concept-definition-1', concept_name, tbox))

    def get_concept_definition1_(self, concept_name=None, tbox=None) -> RacerResult:
        return self.racer_call('get-concept-definition-1', concept_name, tbox)

    def get_concept_negated_definition1(self, concept_name=None, tbox=None) -> str:
        return str(self.racer_call('get-concept-negated-definition-1', concept_name, tbox))

    def get_concept_negated_definition1_(self, concept_name=None, tbox=None) -> RacerResult:
        return self.racer_call('get-concept-negated-definition-1', concept_name, tbox)

    def get_concept_pmodel(self, concept_expr=None, tbox=None) -> str:
        return str(self.racer_call('get-concept-pmodel', concept_expr, tbox))

    def get_concept_pmodel_(self, concept_expr=None, tbox=None) -> RacerResult:
        return self.racer_call('get-concept-pmodel', concept_expr, tbox)

    def get_concept_properties(self, *key_args) -> str:
        return str(self.racer_call('get-concept-properties', key_args))

    def get_concept_properties_(self, *key_args) -> RacerResult:
        return self.racer_call('get-concept-properties', key_args)

    def get_current_set_of_rule_consequences(self, query=None) -> str:
        return str(self.racer_call('get-current-set-of-rule-consequences', query))

    def get_current_set_of_rule_consequences_(self, query=None) -> RacerResult:
        return self.racer_call('get-current-set-of-rule-consequences', query)

    def get_current_tuple(self, query=None) -> str:
        return str(self.racer_call('get-current-tuple', query))

    def get_current_tuple_(self, query=None) -> RacerResult:
        return self.racer_call('get-current-tuple', query)

    def get_dag_of_qbox_for_abox(self, abox=None) -> str:
        return str(self.racer_call('get-dag-of-qbox-for-abox', abox))

    def get_dag_of_qbox_for_abox_(self, abox=None) -> RacerResult:
        return self.racer_call('get-dag-of-qbox-for-abox', abox)

    def get_data_bottom_role(self, tbox=None) -> str:
        return str(self.racer_call('get-data-bottom-role', tbox))

    def get_data_bottom_role_(self, tbox=None) -> RacerResult:
        return self.racer_call('get-data-bottom-role', tbox)

    def get_data_edge_description(self, *key_args) -> str:
        return str(self.racer_call('get-data-edge-description', key_args))

    def get_data_edge_description_(self, *key_args) -> RacerResult:
        return self.racer_call('get-data-edge-description', key_args)

    def get_data_edge_label(self, *key_args) -> str:
        return str(self.racer_call('get-data-edge-label', key_args))

    def get_data_edge_label_(self, *key_args) -> RacerResult:
        return self.racer_call('get-data-edge-label', key_args)

    def get_data_node_description(self, *key_args) -> str:
        return str(self.racer_call('get-data-node-description', key_args))

    def get_data_node_description_(self, *key_args) -> RacerResult:
        return self.racer_call('get-data-node-description', key_args)

    def get_data_node_label(self, *key_args) -> str:
        return str(self.racer_call('get-data-node-label', key_args))

    def get_data_node_label_(self, *key_args) -> RacerResult:
        return self.racer_call('get-data-node-label', key_args)

    def get_edge_label_for_non_existent_edges(self, *key_args) -> str:
        return str(self.racer_call('get-edge-label-for-non-existent-edges', key_args))

    def get_edge_label_for_non_existent_edges_(self, *key_args) -> RacerResult:
        return self.racer_call('get-edge-label-for-non-existent-edges', key_args)

    def get_explanations(self, *key_args) -> str:
        return str(self.racer_call('get-explanations', key_args))

    def get_explanations_(self, *key_args) -> RacerResult:
        return self.racer_call('get-explanations', key_args)

    def get_individual_annotation_datatype_fillers(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('get-individual-annotation-datatype-fillers', individual_name, abox))

    def get_individual_annotation_datatype_fillers_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('get-individual-annotation-datatype-fillers', individual_name, abox)

    def get_individual_annotation_fillers(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('get-individual-annotation-fillers', individual_name, abox))

    def get_individual_annotation_fillers_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('get-individual-annotation-fillers', individual_name, abox)

    def get_individual_datatype_fillers(self, individual_name=None, abox=None, with_types_p=None) -> str:
        return str(self.racer_call('get-individual-datatype-fillers', individual_name, abox, with_types_p))

    def get_individual_datatype_fillers_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('get-individual-datatype-fillers', individual_name, abox)

    def get_individual_pmodel(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('get-individual-pmodel', individual_name, abox))

    def get_individual_pmodel_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('get-individual-pmodel', individual_name, abox)

    def get_individual_successors(self, *key_args) -> str:
        return str(self.racer_call('get-individual-successors', key_args))

    def get_individual_successors_(self, *key_args) -> RacerResult:
        return self.racer_call('get-individual-successors', key_args)

    def get_initial_size_of_process_pool(self) -> str:
        return str(self.racer_call('get-initial-size-of-process-pool'))

    def get_initial_size_of_process_pool_(self) -> RacerResult:
        return self.racer_call('get-initial-size-of-process-pool')

    def get_kb_signature(self, kb_name=None) -> str:
        return str(self.racer_call('get-kb-signature', kb_name))

    def get_kb_signature_(self, kb_name=None) -> RacerResult:
        return self.racer_call('get-kb-signature', kb_name)

    def get_max_no_of_tuples_bound(self) -> str:
        return str(self.racer_call('get-max-no-of-tuples-bound'))

    def get_max_no_of_tuples_bound_(self) -> RacerResult:
        return self.racer_call('get-max-no-of-tuples-bound')

    def get_maximum(self, *key_args) -> str:
        return str(self.racer_call('get-maximum', key_args))

    def get_maximum_(self, *key_args) -> RacerResult:
        return self.racer_call('get-maximum', key_args)

    def get_maximum_size_of_process_pool(self) -> str:
        return str(self.racer_call('get-maximum-size-of-process-pool'))

    def get_maximum_size_of_process_pool_(self) -> RacerResult:
        return self.racer_call('get-maximum-size-of-process-pool')

    def get_meta_constraint(self, tbox=None) -> str:
        return str(self.racer_call('get-meta-constraint', tbox))

    def get_meta_constraint_(self, tbox=None) -> RacerResult:
        return self.racer_call('get-meta-constraint', tbox)

    def get_minimum(self, *key_args) -> str:
        return str(self.racer_call('get-minimum', key_args))

    def get_minimum_(self, *key_args) -> RacerResult:
        return self.racer_call('get-minimum', key_args)

    def get_namespace_prefix(self, tbox=None) -> str:
        return str(self.racer_call('get-namespace-prefix', tbox))

    def get_namespace_prefix_(self, tbox=None) -> RacerResult:
        return self.racer_call('get-namespace-prefix', tbox)

    def get_new_ind_counter(self) -> str:
        return str(self.racer_call('get-new-ind-counter'))

    def get_new_ind_counter_(self) -> RacerResult:
        return self.racer_call('get-new-ind-counter')

    def get_new_ind_prefix(self) -> str:
        return str(self.racer_call('get-new-ind-prefix'))

    def get_new_ind_prefix_(self) -> RacerResult:
        return self.racer_call('get-new-ind-prefix')

    def get_next_n_remaining_sets_of_rule_consequences(self, query=None, n=None) -> str:
        return str(self.racer_call('get-next-n-remaining-sets-of-rule-consequences', query, n))

    def get_next_n_remaining_sets_of_rule_consequences_(self, query=None, n=None) -> RacerResult:
        return self.racer_call('get-next-n-remaining-sets-of-rule-consequences', query, n)

    def get_next_n_remaining_tuples(self, *key_args) -> str:
        return str(self.racer_call('get-next-n-remaining-tuples', key_args))

    def get_next_n_remaining_tuples_(self, *key_args) -> RacerResult:
        return self.racer_call('get-next-n-remaining-tuples', key_args)

    def get_next_set_of_rule_consequences(self, query=None) -> str:
        return str(self.racer_call('get-next-set-of-rule-consequences', query))

    def get_next_set_of_rule_consequences_(self, query=None) -> RacerResult:
        return self.racer_call('get-next-set-of-rule-consequences', query)

    def get_next_tuple(self, *key_args) -> str:
        return str(self.racer_call('get-next-tuple', key_args))

    def get_next_tuple_(self, *key_args) -> RacerResult:
        return self.racer_call('get-next-tuple', key_args)

    def get_nodes_in_qbox_for_abox(self, abox=None) -> str:
        return str(self.racer_call('get-nodes-in-qbox-for-abox', abox))

    def get_nodes_in_qbox_for_abox_(self, abox=None) -> RacerResult:
        return self.racer_call('get-nodes-in-qbox-for-abox', abox)

    def get_nrql_version(self) -> str:
        return str(self.racer_call('get-nrql-version'))

    def get_nrql_version_(self) -> RacerResult:
        return self.racer_call('get-nrql-version')

    def get_number_of_explanations(self, *key_args) -> str:
        return str(self.racer_call('get-number-of-explanations', key_args))

    def get_number_of_explanations_(self, *key_args) -> RacerResult:
        return self.racer_call('get-number-of-explanations', key_args)

    def get_object_bottom_role(self, tbox=None) -> str:
        return str(self.racer_call('get-object-bottom-role', tbox))

    def get_object_bottom_role_(self, tbox=None) -> RacerResult:
        return self.racer_call('get-object-bottom-role', tbox)

    def get_prefixes(self, tbox=None, ask_owlapi_p=None) -> str:
        return str(self.racer_call('get-prefixes', tbox, ask_owlapi_p))

    def get_prefixes_(self, tbox=None, ask_owlapi_p=None) -> RacerResult:
        return self.racer_call('get-prefixes', tbox, ask_owlapi_p)

    def get_process_pool_size(self) -> str:
        return str(self.racer_call('get-process-pool-size'))

    def get_process_pool_size_(self) -> RacerResult:
        return self.racer_call('get-process-pool-size')

    def get_proxy_server(self) -> str:
        return str(self.racer_call('get-proxy-server'))

    def get_proxy_server_(self) -> RacerResult:
        return self.racer_call('get-proxy-server')

    def get_role_datatype(self, role_name=None, tbox=None) -> str:
        return str(self.racer_call('get-role-datatype', role_name, tbox))

    def get_role_datatype_(self, role_name=None, tbox=None) -> RacerResult:
        return self.racer_call('get-role-datatype', role_name, tbox)

    def get_role_hierarchy(self, *key_args) -> str:
        return str(self.racer_call('get-role-hierarchy', key_args))

    def get_role_hierarchy_(self, *key_args) -> RacerResult:
        return self.racer_call('get-role-hierarchy', key_args)

    def get_server_timeout(self) -> str:
        return str(self.racer_call('get-server-timeout'))

    def get_server_timeout_(self) -> RacerResult:
        return self.racer_call('get-server-timeout')

    def get_substrate_edges(self, *key_args) -> str:
        return str(self.racer_call('get-substrate-edges', key_args))

    def get_substrate_edges_(self, *key_args) -> RacerResult:
        return self.racer_call('get-substrate-edges', key_args)

    def get_substrate_nodes(self, *key_args) -> str:
        return str(self.racer_call('get-substrate-nodes', key_args))

    def get_substrate_nodes_(self, *key_args) -> RacerResult:
        return self.racer_call('get-substrate-nodes', key_args)

    def get_substrate_type(self) -> str:
        return str(self.racer_call('get-substrate-type'))

    def get_substrate_type_(self) -> RacerResult:
        return self.racer_call('get-substrate-type')

    def get_tbox_language(self, tbox=None) -> str:
        return str(self.racer_call('get-tbox-language', tbox))

    def get_tbox_language_(self, tbox=None) -> RacerResult:
        return self.racer_call('get-tbox-language', tbox)

    def get_tbox_signature(self, tbox=None) -> str:
        return str(self.racer_call('get-tbox-signature', tbox))

    def get_tbox_signature_(self, tbox=None) -> RacerResult:
        return self.racer_call('get-tbox-signature', tbox)

    def get_tbox_version(self, tbox=None) -> str:
        return str(self.racer_call('get-tbox-version', tbox))

    def get_tbox_version_(self, tbox=None) -> RacerResult:
        return self.racer_call('get-tbox-version', tbox)

    def in_unsafe_mode_p(self) -> bool:
        return self.return_boolean(self.racer_call('in-unsafe-mode?'))

    def inaccurate_queries(self, *key_args) -> str:
        return str(self.racer_call('inaccurate-queries', key_args))

    def inaccurate_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('inaccurate-queries', key_args)

    def inaccurate_rules(self, *key_args) -> str:
        return str(self.racer_call('inaccurate-rules', key_args))

    def inaccurate_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('inaccurate-rules', key_args)

    def include_kb(self, pathname=None) -> str:
        return str(self.racer_call('include-kb', pathname))

    def include_kb_(self, pathname=None) -> RacerResult:
        return self.racer_call('include-kb', pathname)

    def include_permutations(self) -> str:
        return str(self.racer_call('include-permutations'))

    def include_permutations_(self) -> RacerResult:
        return self.racer_call('include-permutations')

    def index_all_triples(self, *key_args) -> str:
        return str(self.racer_call('index-all-triples', key_args))

    def index_all_triples_(self, *key_args) -> RacerResult:
        return self.racer_call('index-all-triples', key_args)

    def individual_instance_p(self, individual_name=None, concept=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('individual-instance-p', individual_name, concept, abox))

    def individual_p(self, individual_name=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('individual-p', individual_name, abox))

    def individuals_equal_p(self, individual1=None, individual2=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('individuals-equal-p', individual1, individual2, abox))

    def individuals_not_equal_p(self, individual1=None, individual2=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('individuals-not-equal-p', individual1, individual2, abox))

    def individuals_related_p(self, ind_predecessor_name_set=None, ind_filler_name_set=None, role_term=None, abox=None) -> bool:
        return self.return_boolean( self.racer_call('individuals-related-p', ind_predecessor_name_set, ind_filler_name_set, role_term, abox))

    def init_abox(self, abox=None, tbox=None) -> str:
        return str(self.racer_call('init-abox', abox, tbox))

    def init_abox_(self, abox=None, tbox=None) -> RacerResult:
        return self.racer_call('init-abox', abox, tbox)

    def init_publications1(self, abox=None) -> str:
        return str(self.racer_call('init-publications-1', abox))

    def init_publications1_(self, abox=None) -> RacerResult:
        return self.racer_call('init-publications-1', abox)

    def init_subscriptions1(self, abox=None) -> str:
        return str(self.racer_call('init-subscriptions-1', abox))

    def init_subscriptions1_(self, abox=None) -> RacerResult:
        return self.racer_call('init-subscriptions-1', abox)

    def init_tbox(self, *key_args) -> str:
        return str(self.racer_call('init-tbox', key_args))

    def init_tbox_(self, *key_args) -> RacerResult:
        return self.racer_call('init-tbox', key_args)

    def installed_patches(self) -> str:
        return str(self.racer_call('installed-patches'))

    def installed_patches_(self) -> RacerResult:
        return self.racer_call('installed-patches')

    def installed_plugins(self) -> str:
        return str(self.racer_call('installed-plugins'))

    def installed_plugins_(self) -> RacerResult:
        return self.racer_call('installed-plugins')

    def instantiators(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('instantiators', individual_name, abox))

    def instantiators_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('instantiators', individual_name, abox)

    def internal_individuals_related_p(self, ind_predecessor_name_set=None, ind_filler_name_set=None, role_term=None, abox=None, check_p=None) -> bool:
        return self.return_boolean( self.racer_call('internal-individuals-related-p', ind_predecessor_name_set, ind_filler_name_set, role_term, abox, check_p))

    def inverse_feature_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('inverse-feature-p', role_term, tbox))

    def inverse_of_role(self, rolename=None, inverse_role=None, tbox=None) -> str:
        return str(self.racer_call('inverse-of-role', rolename, inverse_role, tbox))

    def inverse_of_role_(self, rolename=None, inverse_role=None, tbox=None) -> RacerResult:
        return self.racer_call('inverse-of-role', rolename, inverse_role, tbox)

    def irreflexive_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('irreflexive-p', role_term, tbox))

    def kb_ontologies(self, kb_name=None) -> str:
        return str(self.racer_call('kb-ontologies', kb_name))

    def kb_ontologies_(self, kb_name=None) -> RacerResult:
        return self.racer_call('kb-ontologies', kb_name)

    def keep_defined_query_atoms(self) -> str:
        return str(self.racer_call('keep-defined-query-atoms'))

    def keep_defined_query_atoms_(self) -> RacerResult:
        return self.racer_call('keep-defined-query-atoms')

    def lcs(self, concept1=None, concept2=None) -> str:
        return str(self.racer_call('lcs', concept1, concept2))

    def lcs_(self, concept1=None, concept2=None) -> RacerResult:
        return self.racer_call('lcs', concept1, concept2)

    def lcs_unfold(self, concept1=None, concept2=None, tbox=None) -> str:
        return str(self.racer_call('lcs-unfold', concept1, concept2, tbox))

    def lcs_unfold_(self, concept1=None, concept2=None, tbox=None) -> RacerResult:
        return self.racer_call('lcs-unfold', concept1, concept2, tbox)

    def load_racer_patch(self, fn=None) -> str:
        return str(self.racer_call('load-racer-patch', fn))

    def load_racer_patch_(self, fn=None) -> RacerResult:
        return self.racer_call('load-racer-patch', fn)

    def load_racer_patches(self, directory=None) -> str:
        return str(self.racer_call('load-racer-patches', directory))

    def load_racer_patches_(self, directory=None) -> RacerResult:
        return self.racer_call('load-racer-patches', directory)

    def load_racer_plugin(self, fn=None) -> str:
        return str(self.racer_call('load-racer-plugin', fn))

    def load_racer_plugin_(self, fn=None) -> RacerResult:
        return self.racer_call('load-racer-plugin', fn)

    def load_racer_plugins(self, directory=None) -> str:
        return str(self.racer_call('load-racer-plugins', directory))

    def load_racer_plugins_(self, directory=None) -> RacerResult:
        return self.racer_call('load-racer-plugins', directory)

    def logging_off(self) -> str:
        return str(self.racer_call('logging-off'))

    def logging_off_(self) -> RacerResult:
        return self.racer_call('logging-off')

    def logging_on(self, filename=None, debug=None) -> str:
        return str(self.racer_call('logging-on', filename, debug))

    def logging_on_(self, filename=None, debug=None) -> RacerResult:
        return self.racer_call('logging-on', filename, debug)

    def make_abduction_rule_from_aboxes(self, *key_args) -> str:
        return str(self.racer_call('make-abduction-rule-from-aboxes', key_args))

    def make_abduction_rule_from_aboxes_(self, *key_args) -> RacerResult:
        return self.racer_call('make-abduction-rule-from-aboxes', key_args)

    def make_backward_rule_from_aboxes(self, precond_abox=None, postcond_abox=None, for_abox=None) -> str:
        return str(self.racer_call('make-backward-rule-from-aboxes', precond_abox, postcond_abox, for_abox))

    def make_backward_rule_from_aboxes_(self, *key_args) -> RacerResult:
        return self.racer_call('make-backward-rule-from-aboxes', key_args)

    def make_forward_rule_from_aboxes(self, precond_abox=None, postcond_abox=None, for_abox=None) -> str:
        return str(self.racer_call('make-forward-rule-from-aboxes', precond_abox, postcond_abox, for_abox))

    def make_forward_rule_from_aboxes_(self, *key_args) -> RacerResult:
        return self.racer_call('make-forward-rule-from-aboxes', key_args)

    def make_plugin_from_fasl_file(self, *key_args) -> str:
        return str(self.racer_call('make-plugin-from-fasl-file', key_args))

    def make_plugin_from_fasl_file_(self, *key_args) -> RacerResult:
        return self.racer_call('make-plugin-from-fasl-file', key_args)

    def make_query_from_abox(self, *key_args) -> str:
        return str(self.racer_call('make-query-from-abox', key_args))

    def make_query_from_abox_(self, *key_args) -> RacerResult:
        return self.racer_call('make-query-from-abox', key_args)

    def materialize_inferences(self, *key_args) -> str:
        return str(self.racer_call('materialize-inferences', key_args))

    def materialize_inferences_(self, *key_args) -> RacerResult:
        return self.racer_call('materialize-inferences', key_args)

    def mirror(self, url_spec1=None, url_or_filename=None) -> str:
        return str(self.racer_call('mirror', url_spec1, url_or_filename))

    def mirror_(self, url_spec1=None, url_or_filename=None) -> RacerResult:
        return self.racer_call('mirror', url_spec1, url_or_filename)

    def most_specific_instantiators(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('most-specific-instantiators', individual_name, abox))

    def most_specific_instantiators_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('most-specific-instantiators', individual_name, abox)

    def move_rules(self, *key_args) -> str:
        return str(self.racer_call('move-rules', key_args))

    def move_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('move-rules', key_args)

    def msc_k(self, *key_args) -> str:
        return str(self.racer_call('msc-k', key_args))

    def msc_k_(self, *key_args) -> RacerResult:
        return self.racer_call('msc-k', key_args)

    def next_set_of_rule_consequences_available_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('next-set-of-rule-consequences-available-p', query))

    def next_tuple_available_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('next-tuple-available-p', query))

    def node_description1(self, name=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('node-description1', name, abox, type_of_substrate))

    def node_description1_(self, name=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('node-description1', name, abox, type_of_substrate)

    def node_label1(self, name=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('node-label1', name, abox, type_of_substrate))

    def node_label1_(self, name=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('node-label1', name, abox, type_of_substrate)

    def open_triple_store(self, *key_args) -> str:
        return str(self.racer_call('open-triple-store', key_args))

    def open_triple_store_(self, *key_args) -> RacerResult:
        return self.racer_call('open-triple-store', key_args)

    def optimizer_dont_ensure_late_lambda_evaluation(self) -> str:
        return str(self.racer_call('optimizer-dont-ensure-late-lambda-evaluation'))

    def optimizer_dont_ensure_late_lambda_evaluation_(self) -> RacerResult:
        return self.racer_call('optimizer-dont-ensure-late-lambda-evaluation')

    def optimizer_dont_use_cardinality_heuristics(self) -> str:
        return str(self.racer_call('optimizer-dont-use-cardinality-heuristics'))

    def optimizer_dont_use_cardinality_heuristics_(self) -> RacerResult:
        return self.racer_call('optimizer-dont-use-cardinality-heuristics')

    def optimizer_ensure_late_lambda_evaluation(self) -> str:
        return str(self.racer_call('optimizer-ensure-late-lambda-evaluation'))

    def optimizer_ensure_late_lambda_evaluation_(self) -> RacerResult:
        return self.racer_call('optimizer-ensure-late-lambda-evaluation')

    def optimizer_get_no_of_plans_upper_bound(self) -> str:
        return str(self.racer_call('optimizer-get-no-of-plans-upper-bound'))

    def optimizer_get_no_of_plans_upper_bound_(self) -> RacerResult:
        return self.racer_call('optimizer-get-no-of-plans-upper-bound')

    def optimizer_get_time_bound(self) -> str:
        return str(self.racer_call('optimizer-get-time-bound'))

    def optimizer_get_time_bound_(self) -> RacerResult:
        return self.racer_call('optimizer-get-time-bound')

    def optimizer_set_no_of_plans_upper_bound(self, n=None) -> str:
        return str(self.racer_call('optimizer-set-no-of-plans-upper-bound', n))

    def optimizer_set_no_of_plans_upper_bound_(self, n=None) -> RacerResult:
        return self.racer_call('optimizer-set-no-of-plans-upper-bound', n)

    def optimizer_set_time_bound(self, n=None) -> str:
        return str(self.racer_call('optimizer-set-time-bound', n))

    def optimizer_set_time_bound_(self, n=None) -> RacerResult:
        return self.racer_call('optimizer-set-time-bound', n)

    def optimizer_use_cardinality_heuristics(self) -> str:
        return str(self.racer_call('optimizer-use-cardinality-heuristics'))

    def optimizer_use_cardinality_heuristics_(self) -> RacerResult:
        return self.racer_call('optimizer-use-cardinality-heuristics')

    def original_query_body(self, query=None) -> str:
        return str(self.racer_call('original-query-body', query))

    def original_query_body_(self, query=None) -> RacerResult:
        return self.racer_call('original-query-body', query)

    def original_query_head(self, query=None) -> str:
        return str(self.racer_call('original-query-head', query))

    def original_query_head_(self, query=None) -> RacerResult:
        return self.racer_call('original-query-head', query)

    def original_rule_antecedence(self, query=None) -> str:
        return str(self.racer_call('original-rule-antecedence', query))

    def original_rule_antecedence_(self, query=None) -> RacerResult:
        return self.racer_call('original-rule-antecedence', query)

    def original_rule_consequence(self, query=None) -> str:
        return str(self.racer_call('original-rule-consequence', query))

    def original_rule_consequence_(self, query=None) -> RacerResult:
        return self.racer_call('original-rule-consequence', query)

    def owl_read_document(self, *key_args) -> str:
        return str(self.racer_call('owl-read-document', key_args))

    def owl_read_document_(self, *key_args) -> RacerResult:
        return self.racer_call('owl-read-document', key_args)

    def owl_read_file(self, *key_args) -> str:
        return str(self.racer_call('owl-read-file', key_args))

    def owl_read_file_(self, *key_args) -> RacerResult:
        return self.racer_call('owl-read-file', key_args)

    def owlapi_add_axiom(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-add_axiom|'))

    def owlapi_add_axiom_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-add_axiom|')

    def owlapi_add_axioms(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-add_axioms|'))

    def owlapi_add_axioms_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-add_axioms|')

    def owlapi_add_prefix(self, prefix=None, namespace=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-add_prefix|', prefix, namespace, reasoner))

    def owlapi_add_prefix_(self, prefix=None, namespace=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-add_prefix|', prefix, namespace, reasoner)

    def owlapi_advance_progress(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-advance_progress|', reasoner))

    def owlapi_advance_progress_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-advance_progress|', reasoner)

    def owlapi_apply_changes(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-apply_changes|', reasoner))

    def owlapi_apply_changes_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-apply_changes|', reasoner)

    def owlapi_auto_add_axioms_to(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-auto_add_axioms_to|', ontology, reasoner))

    def owlapi_auto_add_axioms_to_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-auto_add_axioms_to|', ontology, reasoner)

    def owlapi_auto_apply_changes(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-auto_apply_changes|', reasoner))

    def owlapi_auto_apply_changes_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-auto_apply_changes|', reasoner)

    def owlapi_auto_batch_add_axioms_to(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-auto_batch_add_axioms_to|', ontology, reasoner))

    def owlapi_auto_batch_add_axioms_to_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-auto_batch_add_axioms_to|', ontology, reasoner)

    def owlapi_auto_batch_remove_axioms_from(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-auto_batch_remove_axioms_from|', ontology, reasoner))

    def owlapi_auto_batch_remove_axioms_from_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-auto_batch_remove_axioms_from|', ontology, reasoner)

    def owlapi_auto_remove_axioms_from(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-auto_remove_axioms_from|', ontology, reasoner))

    def owlapi_auto_remove_axioms_from_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-auto_remove_axioms_from|', ontology, reasoner)

    def owlapi_axiom_loaded_p(self, id=None, reasoner=None) -> bool:
        return self.return_boolean(self.racer_call('|_o_w_l_a_p_i-_axiom_loaded?|', id, reasoner))

    def owlapi_axiom_to_i_d(self, axiom_constructor_call=None, reasoner=None, ont=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-_axiom_to_i_d|', axiom_constructor_call, reasoner, ont))

    def owlapi_axiom_to_i_d_(self, axiom_constructor_call=None, reasoner=None, ont=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-_axiom_to_i_d|', axiom_constructor_call, reasoner, ont)

    def owlapi_batch_synchronize(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-batch_synchronize|', ontology, reasoner))

    def owlapi_batch_synchronize_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-batch_synchronize|', ontology, reasoner)

    def owlapi_clear_changes(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-clear_changes|', reasoner))

    def owlapi_clear_changes_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-clear_changes|', reasoner)

    def owlapi_clear_ontologies(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-clear_ontologies|', reasoner))

    def owlapi_clear_ontologies_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-clear_ontologies|', reasoner)

    def owlapi_clear_registry(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-clear_registry|', reasoner))

    def owlapi_clear_registry_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-clear_registry|', reasoner)

    def owlapi_consider_declarations(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-consider_declarations|', reasoner))

    def owlapi_consider_declarations_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-consider_declarations|', reasoner)

    def owlapi_describe_ontologies(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-describe_ontologies|', reasoner))

    def owlapi_describe_ontologies_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-describe_ontologies|', reasoner)

    def owlapi_describe_ontology(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-describe_ontology|', ontology, reasoner))

    def owlapi_describe_ontology_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-describe_ontology|', ontology, reasoner)

    def owlapi_describe_reasoner(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-describe_reasoner|', reasoner))

    def owlapi_describe_reasoner_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-describe_reasoner|', reasoner)

    def owlapi_describe_reasoners(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-describe_reasoners|'))

    def owlapi_describe_reasoners_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-describe_reasoners|')

    def owlapi_disable_auto_mode(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-disable_auto_mode|', reasoner))

    def owlapi_disable_auto_mode_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-disable_auto_mode|', reasoner)

    def owlapi_disable_incremental_updates(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-disable_incremental_updates|', reasoner))

    def owlapi_disable_incremental_updates_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-disable_incremental_updates|', reasoner)

    def owlapi_disable_lookup_mode(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-disable_lookup_mode|', reasoner))

    def owlapi_disable_lookup_mode_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-disable_lookup_mode|', reasoner)

    def owlapi_disable_memory_saving_mode(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-disable_memory_saving_mode|', reasoner))

    def owlapi_disable_memory_saving_mode_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-disable_memory_saving_mode|', reasoner)

    def owlapi_disable_simplified_protocol(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-disable_simplified_protocol|', reasoner))

    def owlapi_disable_simplified_protocol_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-disable_simplified_protocol|', reasoner)

    def owlapi_disable_transient_axiom_mode(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-disable_transient_axiom_mode|', reasoner))

    def owlapi_disable_transient_axiom_mode_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-disable_transient_axiom_mode|', reasoner)

    def owlapi_dispose_axiom(self, id_or_constructor=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-dispose_axiom|', id_or_constructor, reasoner))

    def owlapi_dispose_axiom_(self, id_or_constructor=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-dispose_axiom|', id_or_constructor, reasoner)

    def owlapi_dispose_axioms(self, ids_or_constructors=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-dispose_axioms|', ids_or_constructors, reasoner))

    def owlapi_dispose_axioms_(self, ids_or_constructors=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-dispose_axioms|', ids_or_constructors, reasoner)

    def owlapi_dispose_ontologies(self, ontologies=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-dispose_ontologies|', ontologies, reasoner))

    def owlapi_dispose_ontologies_(self, ontologies=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-dispose_ontologies|', ontologies, reasoner)

    def owlapi_dispose_ontology(self, ont_name=None, reasoner=None, dispose_axioms_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-dispose_ontology|', ont_name, reasoner, dispose_axioms_p))

    def owlapi_dispose_ontology_(self, ont_name=None, reasoner=None, dispose_axioms_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-dispose_ontology|', ont_name, reasoner, dispose_axioms_p)

    def owlapi_dispose_reasoner(self, name=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-dispose_reasoner|', name))

    def owlapi_dispose_reasoner_(self, name=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-dispose_reasoner|', name)

    def owlapi_dont_register_declared_entities(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-dont_register_declared_entities|', reasoner))

    def owlapi_dont_register_declared_entities_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-dont_register_declared_entities|', reasoner)

    def owlapi_dont_register_referenced_entities(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-dont_register_referenced_entities|', reasoner))

    def owlapi_dont_register_referenced_entities_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-dont_register_referenced_entities|', reasoner)

    def owlapi_enable_incremental_updates(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-enable_incremental_updates|', reasoner))

    def owlapi_enable_incremental_updates_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-enable_incremental_updates|', reasoner)

    def owlapi_enable_lookup_mode(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-enable_lookup_mode|', reasoner))

    def owlapi_enable_lookup_mode_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-enable_lookup_mode|', reasoner)

    def owlapi_enable_memory_saving_mode(self, ontology=None, reasoner=None, use_less_tbox_memory_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-enable_memory_saving_mode|', ontology, reasoner, use_less_tbox_memory_p))

    def owlapi_enable_memory_saving_mode_(self, ontology=None, reasoner=None, use_less_tbox_memory_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-enable_memory_saving_mode|', ontology, reasoner, use_less_tbox_memory_p)

    def owlapi_enable_simplified_protocol(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-enable_simplified_protocol|', reasoner))

    def owlapi_enable_simplified_protocol_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-enable_simplified_protocol|', reasoner)

    def owlapi_enable_transient_axiom_mode(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-enable_transient_axiom_mode|', reasoner))

    def owlapi_enable_transient_axiom_mode_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-enable_transient_axiom_mode|', reasoner)

    def owlapi_export_ontology(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-export_ontology|', key_args))

    def owlapi_export_ontology_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-export_ontology|', key_args)

    def owlapi_export_reasoner(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-export_reasoner|', key_args))

    def owlapi_export_reasoner_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-export_reasoner|', key_args)

    def owlapi_find_i_d_from_object(self, obj=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-find_i_d_from_object|', obj))

    def owlapi_find_i_d_from_object_(self, obj=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-find_i_d_from_object|', obj)

    def owlapi_find_object_from_i_d(self, id=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-find_object_from_i_d|', id))

    def owlapi_find_object_from_i_d_(self, id=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-find_object_from_i_d|', id)

    def owlapi_get_all_ontologies(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_all_ontologies|'))

    def owlapi_get_all_ontologies_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_all_ontologies|')

    def owlapi_get_ancestor_classes(self, cls=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_ancestor_classes|', cls, reasoner))

    def owlapi_get_ancestor_classes_(self, cls=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_ancestor_classes|', cls, reasoner)

    def owlapi_get_ancestor_properties(self, property_=None, reasoner=None, remove_self_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_ancestor_properties|', property_, reasoner, remove_self_p))

    def owlapi_get_ancestor_properties_(self, property_=None, reasoner=None, remove_self_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_ancestor_properties|', property_, reasoner, remove_self_p)

    def owlapi_get_annotation_axioms_for_axiom(self, axiom_id=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_annotation_axioms_for_axiom|', axiom_id, reasoner))

    def owlapi_get_annotation_axioms_for_axiom_(self, axiom_id=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_annotation_axioms_for_axiom|', axiom_id, reasoner)

    def owlapi_get_auto_declare_data_properties(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_auto_declare_data_properties|', reasoner))

    def owlapi_get_auto_declare_data_properties_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_auto_declare_data_properties|', reasoner)

    def owlapi_get_auto_ontology(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_auto_ontology|', reasoner))

    def owlapi_get_auto_ontology_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_auto_ontology|', reasoner)

    def owlapi_get_axiom_counter(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_axiom_counter|', reasoner))

    def owlapi_get_axiom_counter_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_axiom_counter|', reasoner)

    def owlapi_get_axioms(self, reasoner=None, with_ids_p=None, with_ont_names_p=None, status=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_axioms|', reasoner, with_ids_p, with_ont_names_p, status))

    def owlapi_get_axioms_(self, reasoner=None, with_ids_p=None, with_ont_names_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_axioms|', reasoner, with_ids_p, with_ont_names_p)

    def owlapi_get_axioms_in(self, ont=None, reasoner=None, with_ids_p=None, status=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_axioms_in|', ont, reasoner, with_ids_p, status))

    def owlapi_get_axioms_in_(self, ont=None, reasoner=None, with_ids_p=None, status=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_axioms_in|', ont, reasoner, with_ids_p, status)

    def owlapi_get_axioms_of_type(self, type_or_types=None, reasoner=None, with_ids_p=None, with_ont_names_p=None, status=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_axioms_of_type|', type_or_types, reasoner, with_ids_p, with_ont_names_p, status))

    def owlapi_get_axioms_of_type_(self, type_or_types=None, reasoner=None, with_ids_p=None, with_ont_names_p=None, status=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_axioms_of_type|', type_or_types, reasoner, with_ids_p, with_ont_names_p, status)

    def owlapi_get_axioms_of_type_in(self, type_or_types=None, ont=None, reasoner=None, with_ids_p=None, status=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_axioms_of_type_in|', type_or_types, ont, reasoner, with_ids_p, status))

    def owlapi_get_axioms_of_type_in_(self, type_or_types=None, ont=None, reasoner=None, with_ids_p=None, status=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_axioms_of_type_in|', type_or_types, ont, reasoner, with_ids_p, status)

    def owlapi_get_axioms_per_ontology(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_axioms_per_ontology|', reasoner))

    def owlapi_get_axioms_per_ontology_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_axioms_per_ontology|', reasoner)

    def owlapi_get_changes(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_changes|', reasoner))

    def owlapi_get_changes_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_changes|', reasoner)

    def owlapi_get_current_reasoner(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_current_reasoner|'))

    def owlapi_get_current_reasoner_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_current_reasoner|')

    def owlapi_get_data_property_relationships(self, ind=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_data_property_relationships|', ind, reasoner))

    def owlapi_get_data_property_relationships_(self, ind=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_data_property_relationships|', ind, reasoner)

    def owlapi_get_data_property_values(self, ind=None, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_data_property_values|', ind, property_, reasoner))

    def owlapi_get_data_property_values_(self, ind=None, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_data_property_values|', ind, property_, reasoner)

    def owlapi_get_descendant_classes(self, cls=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_descendant_classes|', cls, reasoner))

    def owlapi_get_descendant_classes_(self, cls=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_descendant_classes|', cls, reasoner)

    def owlapi_get_descendant_properties(self, property_=None, reasoner=None, remove_self_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_descendant_properties|', property_, reasoner, remove_self_p))

    def owlapi_get_descendant_properties_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_descendant_properties|', property_, reasoner)

    def owlapi_get_different_individuals(self, ind=None, reasoner=None, synonyms=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_different_individuals|', ind, reasoner, synonyms))

    def owlapi_get_different_individuals_(self, ind=None, reasoner=None, synonyms=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_different_individuals|', ind, reasoner, synonyms)

    def owlapi_get_disjoint_classes(self, concept=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_disjoint_classes|', concept, reasoner))

    def owlapi_get_disjoint_classes_(self, concept=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_disjoint_classes|', concept, reasoner)

    def owlapi_get_disjoint_data_properties(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_disjoint_data_properties|', property_, reasoner))

    def owlapi_get_disjoint_data_properties_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_disjoint_data_properties|', property_, reasoner)

    def owlapi_get_disjoint_object_properties(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_disjoint_object_properties|', property_, reasoner))

    def owlapi_get_disjoint_object_properties_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_disjoint_object_properties|', property_, reasoner)

    def owlapi_get_domains(self, property_=None, reasoner=None, owlapi_hacking_mode=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_domains|', property_, reasoner, owlapi_hacking_mode))

    def owlapi_get_domains_(self, property_=None, reasoner=None, owlapi_hacking_mode=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_domains|', property_, reasoner, owlapi_hacking_mode)

    def owlapi_get_equivalent_classes(self, cls=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_equivalent_classes|', cls, reasoner))

    def owlapi_get_equivalent_classes_(self, cls=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_equivalent_classes|', cls, reasoner)

    def owlapi_get_equivalent_properties(self, property_=None, reasoner=None, remove_self_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_equivalent_properties|', property_, reasoner, remove_self_p))

    def owlapi_get_equivalent_properties_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_equivalent_properties|', property_, reasoner, reasoner)

    def owlapi_get_inconsistent_classes(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_inconsistent_classes|', reasoner))

    def owlapi_get_inconsistent_classes_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_inconsistent_classes|', reasoner)

    def owlapi_get_individuals(self, cls1=None, direct=None, cls2=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_individuals|', cls1, direct, cls2, reasoner))

    def owlapi_get_individuals_(self, cls1=None, direct=None, cls2=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_individuals|', cls1, direct, cls2, reasoner)

    def owlapi_get_instances(self, cls3=None, direct=None, cls4=None, reasoner=None, synonyms=None, cls5=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_instances|', cls3, direct, cls4, reasoner, synonyms, cls5))

    def owlapi_get_instances_(self, cls3=None, direct=None, cls4=None, reasoner=None, synonyms=None, cls5=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_instances|', cls3, direct, cls4, reasoner, synonyms, cls5)

    def owlapi_get_inverse_properties(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_inverse_properties|', property_, reasoner))

    def owlapi_get_inverse_properties_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_inverse_properties|', property_, reasoner)

    def owlapi_get_loaded_ontologies(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_loaded_ontologies|', reasoner))

    def owlapi_get_loaded_ontologies_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_loaded_ontologies|', reasoner)

    def owlapi_get_object_property_relationships(self, ind=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_object_property_relationships|', ind, reasoner))

    def owlapi_get_object_property_relationships_(self, ind=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_object_property_relationships|', ind, reasoner)

    def owlapi_get_object_property_values(self, ind=None, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_object_property_values|', ind, property_, reasoner))

    def owlapi_get_object_property_values_(self, ind=None, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_object_property_values|', ind, property_, reasoner)

    def owlapi_get_ontologies(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_ontologies|', reasoner))

    def owlapi_get_ontologies_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_ontologies|', reasoner)

    def owlapi_get_o_w_l_annotation_assertion_axiom(self, annotation_subject=None, annotation_property=None, annotation_value=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_annotation_assertion_axiom|', annotation_subject, annotation_property, annotation_value, reasoner))

    def owlapi_get_o_w_l_annotation_assertion_axiom_(self, annotation_subject=None, annotation_property=None, annotation_value=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_annotation_assertion_axiom|', annotation_subject, annotation_property, annotation_value, reasoner)

    def owlapi_get_o_w_l_annotation_property_domain_axiom(self, annotation_property=None, annotation_property_domain=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_annotation_property_domain_axiom|', annotation_property, annotation_property_domain, reasoner))

    def owlapi_get_o_w_l_annotation_property_domain_axiom_(self, annotation_property=None, annotation_property_domain=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_annotation_property_domain_axiom|', annotation_property, annotation_property_domain, reasoner)

    def owlapi_get_o_w_l_annotation_property_range_axiom(self, annotation_property=None, annotation_property_range=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_annotation_property_range_axiom|', annotation_property, annotation_property_range, reasoner))

    def owlapi_get_o_w_l_annotation_property_range_axiom_(self, annotation_property=None, annotation_property_range=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_annotation_property_range_axiom|', annotation_property, annotation_property_range, reasoner)

    def owlapi_get_o_w_l_asymmetric_object_property_axiom(self, object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_asymmetric_object_property_axiom|', object_property, reasoner))

    def owlapi_get_o_w_l_asymmetric_object_property_axiom_(self, object_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_asymmetric_object_property_axiom|', object_property, reasoner)

    def owlapi_get_o_w_l_axiom_annotation_axiom(self, axiom_id=None, annotation=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_axiom_annotation_axiom|', axiom_id, annotation, reasoner))

    def owlapi_get_o_w_l_axiom_annotation_axiom_(self, axiom_id=None, annotation=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_axiom_annotation_axiom|', axiom_id, annotation, reasoner)

    def owlapi_get_o_w_l_class_assertion_axiom(self, individual=None, description=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_class_assertion_axiom|', individual, description, reasoner))

    def owlapi_get_o_w_l_class_assertion_axiom_(self, individual=None, description=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_class_assertion_axiom|', individual, description, reasoner)

    def owlapi_get_o_w_l_data_property_assertion_axiom(self, subject=None, rel_data_property=None, value=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_property_assertion_axiom|', subject, rel_data_property, value, reasoner))

    def owlapi_get_o_w_l_data_property_assertion_axiom_(self, subject=None, rel_data_property=None, value=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_property_assertion_axiom|', subject, rel_data_property, value, reasoner)

    def owlapi_get_o_w_l_data_property_domain_axiom(self, data_property=None, data_property_domain=None, reasoner=None) -> str:
        return str( self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_property_domain_axiom|', data_property, data_property_domain, reasoner))

    def owlapi_get_o_w_l_data_property_domain_axiom_(self, data_property=None, data_property_domain=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_property_domain_axiom|', data_property, data_property_domain, reasoner)

    def owlapi_get_o_w_l_data_property_range_axiom(self, data_property=None, data_range=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_property_range_axiom|', data_property, data_range, reasoner))

    def owlapi_get_o_w_l_data_property_range_axiom_(self, data_property=None, data_range=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_property_range_axiom|', data_property, data_range, reasoner)

    def owlapi_get_o_w_l_data_sub_property_axiom(self, data_sub_property=None, data_super_property=None, reasoner=None) -> str:
        return str( self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_sub_property_axiom|', data_sub_property, data_super_property, reasoner))

    def owlapi_get_o_w_l_data_sub_property_axiom_(self, data_sub_property=None, data_super_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_data_sub_property_axiom|', data_sub_property, data_super_property, reasoner)

    def owlapi_get_o_w_l_datatype_definition_axiom(self, datatype_name=None, data_range=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_datatype_definition_axiom|', datatype_name, data_range, reasoner))

    def owlapi_get_o_w_l_datatype_definition_axiom_(self, datatype_name=None, data_range=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_datatype_definition_axiom|', datatype_name, data_range, reasoner)

    def owlapi_get_o_w_l_declaration_axiom(self, entity=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_declaration_axiom|', entity, reasoner))

    def owlapi_get_o_w_l_declaration_axiom_(self, entity=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_declaration_axiom|', entity, reasoner)

    def owlapi_get_o_w_l_different_individuals_axiom(self, individuals=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_different_individuals_axiom|', individuals, reasoner))

    def owlapi_get_o_w_l_different_individuals_axiom_(self, individuals=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_different_individuals_axiom|', individuals, reasoner)

    def owlapi_get_o_w_l_disjoint_classes_axiom(self, descriptions=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_classes_axiom|', descriptions, reasoner))

    def owlapi_get_o_w_l_disjoint_classes_axiom_(self, descriptions=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_classes_axiom|', descriptions, reasoner)

    def owlapi_get_o_w_l_disjoint_data_properties_axiom(self, data_properties=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_data_properties_axiom|', data_properties, reasoner))

    def owlapi_get_o_w_l_disjoint_data_properties_axiom_(self, data_properties=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_data_properties_axiom|', data_properties, reasoner)

    def owlapi_get_o_w_l_disjoint_object_properties_axiom(self, object_properties=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_object_properties_axiom|', object_properties, reasoner))

    def owlapi_get_o_w_l_disjoint_object_properties_axiom_(self, object_properties=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_object_properties_axiom|', object_properties, reasoner)

    def owlapi_get_o_w_l_disjoint_union_axiom(self, description=None, descriptions=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_union_axiom|', description, descriptions, reasoner))

    def owlapi_get_o_w_l_disjoint_union_axiom_(self, description=None, descriptions=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_disjoint_union_axiom|', description, descriptions, reasoner)

    def owlapi_get_o_w_l_entity_annotation_axiom(self, entity=None, annotation=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_entity_annotation_axiom|', entity, annotation, reasoner))

    def owlapi_get_o_w_l_entity_annotation_axiom_(self, entity=None, annotation=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_entity_annotation_axiom|', entity, annotation, reasoner)

    def owlapi_get_o_w_l_equivalent_classes_axiom(self, descriptions=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_equivalent_classes_axiom|', descriptions, reasoner))

    def owlapi_get_o_w_l_equivalent_classes_axiom_(self, descriptions=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_equivalent_classes_axiom|', descriptions, reasoner)

    def owlapi_get_o_w_l_equivalent_data_properties_axiom(self, data_properties=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_equivalent_data_properties_axiom|', data_properties, reasoner))

    def owlapi_get_o_w_l_equivalent_data_properties_axiom_(self, data_properties=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_equivalent_data_properties_axiom|', data_properties, reasoner)

    def owlapi_get_o_w_l_equivalent_object_properties_axiom(self, object_properties=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_equivalent_object_properties_axiom|', object_properties, reasoner))

    def owlapi_get_o_w_l_equivalent_object_properties_axiom_(self, object_properties=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_equivalent_object_properties_axiom|', object_properties, reasoner)

    def owlapi_get_o_w_l_functional_data_property_axiom(self, data_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_functional_data_property_axiom|', data_property, reasoner))

    def owlapi_get_o_w_l_functional_data_property_axiom_(self, data_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_functional_data_property_axiom|', data_property, reasoner)

    def owlapi_get_o_w_l_functional_object_property_axiom(self, object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_functional_object_property_axiom|', object_property, reasoner))

    def owlapi_get_o_w_l_functional_object_property_axiom_(self, object_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_functional_object_property_axiom|', object_property, reasoner)

    def owlapi_get_o_w_l_has_key_axiom(self, key_class=None, key_object_properties=None, key_data_properties=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_has_key_axiom|', key_class, key_object_properties, key_data_properties, reasoner))

    def owlapi_get_o_w_l_has_key_axiom_(self, key_class=None, key_object_properties=None, key_data_properties=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_has_key_axiom|', key_class, key_object_properties, key_data_properties, reasoner)

    def owlapi_get_o_w_l_implicit_declaration_axiom(self, entity=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_implicit_declaration_axiom|', entity, reasoner))

    def owlapi_get_o_w_l_implicit_declaration_axiom_(self, entity=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_implicit_declaration_axiom|', entity, reasoner)

    def owlapi_get_o_w_l_imports_declaration_axiom(self, ontology_import_uri=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_imports_declaration_axiom|', ontology_import_uri, reasoner))

    def owlapi_get_o_w_l_imports_declaration_axiom_(self, ontology_import_uri=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_imports_declaration_axiom|', ontology_import_uri, reasoner)

    def owlapi_get_o_w_l_inverse_functional_object_property_axiom(self, object_property=None, reasoner=None) -> str:
        return str( self.racer_call('|_o_w_l_a_p_i-get_o_w_l_inverse_functional_object_property_axiom|', object_property, reasoner))

    def owlapi_get_o_w_l_inverse_functional_object_property_axiom_(self, object_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_inverse_functional_object_property_axiom|', object_property, reasoner)

    def owlapi_get_o_w_l_inverse_object_properties_axiom(self, first_object_property=None, second_object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_inverse_object_properties_axiom|', first_object_property, second_object_property, reasoner))

    def owlapi_get_o_w_l_inverse_object_properties_axiom_(self, first_object_property=None, second_object_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_inverse_object_properties_axiom|', first_object_property, second_object_property, reasoner)

    def owlapi_get_o_w_l_irreflexive_object_property_axiom(self, object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_irreflexive_object_property_axiom|', object_property, reasoner))

    def owlapi_get_o_w_l_irreflexive_object_property_axiom_(self,  object_property=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_irreflexive_object_property_axiom|', object_property)

    def owlapi_get_o_w_l_negative_data_property_assertion_axiom(self, subject=None, rel_data_property=None, value=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_negative_data_property_assertion_axiom|', subject, rel_data_property, value, reasoner))

    def owlapi_get_o_w_l_negative_data_property_assertion_axiom_(self, subject=None, rel_data_property=None, value=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_negative_data_property_assertion_axiom|', subject, rel_data_property, value, reasoner)

    def owlapi_get_o_w_l_negative_object_property_assertion_axiom(self, subject=None, rel_object_property=None, object_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_negative_object_property_assertion_axiom|', subject, rel_object_property, object_, reasoner))

    def owlapi_get_o_w_l_negative_object_property_assertion_axiom_(self, subject=None, rel_object_property=None, object_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_negative_object_property_assertion_axiom|', subject, rel_object_property, object_, reasoner)

    def owlapi_get_o_w_l_object_property_assertion_axiom(self, subject=None, rel_object_property=None, object_=None, reasoner=None) -> str:
        return str( self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_assertion_axiom|', subject, rel_object_property, object_, reasoner))

    def owlapi_get_o_w_l_object_property_assertion_axiom_(self, subject=None, rel_object_property=None, object_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_assertion_axiom|', subject, rel_object_property, object_, reasoner)

    def owlapi_get_o_w_l_object_property_chain_sub_property_axiom(self, object_property_chain=None, object_super_property=None, reasoner=None) -> str:
        return str( self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_chain_sub_property_axiom|', object_property_chain, object_super_property, reasoner))

    def owlapi_get_o_w_l_object_property_chain_sub_property_axiom_(self, object_property_chain=None, object_super_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_chain_sub_property_axiom|', object_property_chain, object_super_property, reasoner)

    def owlapi_get_o_w_l_object_property_domain_axiom(self, object_property=None, object_property_domain=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_domain_axiom|', object_property, object_property_domain, reasoner))

    def owlapi_get_o_w_l_object_property_domain_axiom_(self, object_property=None, object_property_domain=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_domain_axiom|', object_property, object_property_domain, reasoner)

    def owlapi_get_o_w_l_object_property_range_axiom(self, object_property=None, object_property_range=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_range_axiom|', object_property, object_property_range, reasoner))

    def owlapi_get_o_w_l_object_property_range_axiom_(self, object_property=None, object_property_range=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_property_range_axiom|', object_property, object_property_range, reasoner)

    def owlapi_get_o_w_l_object_sub_property_axiom(self, object_sub_property=None, object_super_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_sub_property_axiom|', object_sub_property, object_super_property, reasoner))

    def owlapi_get_o_w_l_object_sub_property_axiom_(self, object_sub_property=None, object_super_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_object_sub_property_axiom|', object_sub_property, object_super_property, reasoner)

    def owlapi_get_o_w_l_ontology_annotation_axiom(self, annotation=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_ontology_annotation_axiom|', annotation, reasoner))

    def owlapi_get_o_w_l_ontology_annotation_axiom_(self, annotation=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_ontology_annotation_axiom|', annotation, reasoner)

    def owlapi_get_o_w_l_ontology_version_declaration_axiom(self, ontology_version_uri=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_ontology_version_declaration_axiom|', ontology_version_uri, reasoner))

    def owlapi_get_o_w_l_ontology_version_declaration_axiom_(self, ontology_version_uri=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_ontology_version_declaration_axiom|', ontology_version_uri, reasoner)

    def owlapi_get_o_w_l_prefix_declaration_axiom(self, namespace_prefix=None, namespace=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_prefix_declaration_axiom|', namespace_prefix, namespace, reasoner))

    def owlapi_get_o_w_l_prefix_declaration_axiom_(self, namespace_prefix=None, namespace=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_prefix_declaration_axiom|', namespace_prefix, namespace, reasoner)

    def owlapi_get_o_w_l_really_implicit_declaration_axiom(self, entity=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_really_implicit_declaration_axiom|', entity, reasoner))

    def owlapi_get_o_w_l_really_implicit_declaration_axiom_(self, entity=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_really_implicit_declaration_axiom|', entity, reasoner)

    def owlapi_get_o_w_l_reflexive_object_property_axiom(self, object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_reflexive_object_property_axiom|', object_property, reasoner))

    def owlapi_get_o_w_l_reflexive_object_property_axiom_(self, object_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_reflexive_object_property_axiom|', object_property, reasoner)

    def owlapi_get_o_w_l_same_individuals_axiom(self, individuals=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_same_individuals_axiom|', individuals, reasoner))

    def owlapi_get_o_w_l_same_individuals_axiom_(self, individuals=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_same_individuals_axiom|', individuals, reasoner)

    def owlapi_get_o_w_l_sub_annotation_property_axiom(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_sub_annotation_property_axiom|'))

    def owlapi_get_o_w_l_sub_annotation_property_axiom_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_sub_annotation_property_axiom|')

    def owlapi_get_o_w_l_sub_annotation_property_of_axiom(self, annotation_sub_property=None, annotation_super_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_sub_annotation_property_of_axiom|', annotation_sub_property, annotation_super_property, reasoner))

    def owlapi_get_o_w_l_sub_annotation_property_of_axiom_(self, annotation_sub_property=None, annotation_super_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_sub_annotation_property_of_axiom|', annotation_sub_property, annotation_super_property, reasoner)

    def owlapi_get_o_w_l_sub_class_axiom(self, sub_class=None, super_class=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_sub_class_axiom|', sub_class, super_class, reasoner))

    def owlapi_get_o_w_l_sub_class_axiom_(self, sub_class=None, super_class=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_sub_class_axiom|', sub_class, super_class, reasoner)

    def owlapi_get_o_w_l_symmetric_object_property_axiom(self, object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_symmetric_object_property_axiom|', object_property, reasoner))

    def owlapi_get_o_w_l_symmetric_object_property_axiom_(self, object_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_symmetric_object_property_axiom|', object_property, reasoner)

    def owlapi_get_o_w_l_transitive_object_property_axiom(self, object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_o_w_l_transitive_object_property_axiom|', object_property, reasoner))

    def owlapi_get_o_w_l_transitive_object_property_axiom_(self, object_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_o_w_l_transitive_object_property_axiom|', object_property, reasoner)

    def owlapi_get_prefixes(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_prefixes|', reasoner))

    def owlapi_get_prefixes_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_prefixes|', reasoner)

    def owlapi_get_ranges(self, property_=None, reasoner=None, owlapi_hacking_mode=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_ranges|', property_, reasoner, owlapi_hacking_mode))

    def owlapi_get_ranges_(self, property_=None, reasoner=None, owlapi_hacking_mode=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_ranges|', property_, reasoner, owlapi_hacking_mode)

    def owlapi_get_reasoners(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_reasoners|'))

    def owlapi_get_reasoners_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_reasoners|')

    def owlapi_get_related_individuals(self, subject=None, object_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_related_individuals|', subject, object_property, reasoner))

    def owlapi_get_related_individuals_(self, subject=None, object_property=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_related_individuals|', subject, object_property)

    def owlapi_get_related_values(self, subject=None, data_property=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_related_values|', subject, data_property, reasoner))

    def owlapi_get_related_values_(self, subject=None, data_property=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_related_values|', subject, data_property, reasoner)

    def owlapi_get_same_individuals(self, ind=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_same_individuals|', ind, reasoner))

    def owlapi_get_same_individuals_(self, ind=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_same_individuals|', ind, reasoner)

    def owlapi_get_sub_classes(self, cls=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_sub_classes|', cls, reasoner))

    def owlapi_get_sub_classes_(self, cls=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_sub_classes|', cls, reasoner)

    def owlapi_get_sub_properties(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_sub_properties|', property_, reasoner))

    def owlapi_get_sub_properties_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_sub_properties|', property_, reasoner)

    def owlapi_get_super_classes(self, cls=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_super_classes|', cls, reasoner))

    def owlapi_get_super_classes_(self, cls=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_super_classes|', cls, reasoner)

    def owlapi_get_super_properties(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_super_properties|', property_, reasoner))

    def owlapi_get_super_properties_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_super_properties|', property_, reasoner)

    def owlapi_get_types(self, individual=None, direct=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_types|', individual, direct, reasoner))

    def owlapi_get_types_(self, individual=None, direct=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_types|', individual, direct, reasoner)

    def owlapi_has_data_property_relationship(self, subject=None, property_=None, object_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-has_data_property_relationship|', subject, property_, object_, reasoner))

    def owlapi_has_data_property_relationship_(self, subject=None, property_=None, object_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-has_data_property_relationship|', subject, property_, object_, reasoner)

    def owlapi_has_object_property_relationship(self, subject=None, property_=None, object_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-has_object_property_relationship|', subject, property_, object_, reasoner))

    def owlapi_has_object_property_relationship_(self, subject=None, property_=None, object_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-has_object_property_relationship|', subject, property_, object_, reasoner)

    def owlapi_has_type(self, ind=None, type_=None, direct=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-has_type|', ind, type_, direct, reasoner))

    def owlapi_has_type_(self, ind=None, type_=None, direct=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-has_type|', ind, type_, direct, reasoner)

    def owlapi_i_d_to_axiom(self, id=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-_i_d_to_axiom|', id, reasoner))

    def owlapi_i_d_to_axiom_(self, id=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-_i_d_to_axiom|', id, reasoner)

    def owlapi_ignore_annotations(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-ignore_annotations|', reasoner))

    def owlapi_ignore_annotations_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-ignore_annotations|', reasoner)

    def owlapi_ignore_declarations(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-ignore_declarations|', reasoner))

    def owlapi_ignore_declarations_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-ignore_declarations|', reasoner)

    def owlapi_is_asymmetric(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_asymmetric|', property_, reasoner))

    def owlapi_is_asymmetric_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_asymmetric|', property_, reasoner)

    def owlapi_is_class(self, clsc=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_class|', clsc, reasoner))

    def owlapi_is_class_(self, clsc=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_class|', clsc, reasoner)

    def owlapi_is_classified(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_classified|', reasoner))

    def owlapi_is_classified_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_classified|', reasoner)

    def owlapi_is_consistent(self, ontology=None, reasoner=None, force_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_consistent|', ontology, reasoner, force_p))

    def owlapi_is_consistent_(self, ontology=None, reasoner=None, force_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_consistent|', ontology, reasoner, force_p)

    def owlapi_is_defined_class(self, cls=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_defined_class|', cls, reasoner))

    def owlapi_is_defined_class_(self, cls=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_defined_class|', cls, reasoner)

    def owlapi_is_defined_data_property(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_defined_data_property|', property_, reasoner))

    def owlapi_is_defined_data_property_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_defined_data_property|', property_, reasoner)

    def owlapi_is_defined_individual(self, ind=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_defined_individual|', ind, reasoner))

    def owlapi_is_defined_individual_(self, ind=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_defined_individual|', ind, reasoner)

    def owlapi_is_defined_object_property(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_defined_object_property|', property_, reasoner))

    def owlapi_is_defined_object_property_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_defined_object_property|', property_, reasoner)

    def owlapi_is_different_individual(self, i=None, j=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_different_individual|', i, j, reasoner))

    def owlapi_is_different_individual_(self, i=None, j=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_different_individual|', i, j, reasoner)

    def owlapi_is_entailed(self, axiom_id_or_constructor=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_entailed|', axiom_id_or_constructor, reasoner))

    def owlapi_is_entailed_(self, axiom_id_or_constructor=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_entailed|', axiom_id_or_constructor, reasoner)

    def owlapi_is_equivalent_class(self, clsc=None, clsd=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_equivalent_class|', clsc, clsd, reasoner))

    def owlapi_is_equivalent_class_(self, clsc=None, clsd=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_equivalent_class|', clsc, clsd, reasoner)

    def owlapi_is_functional(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_functional|', property_, reasoner))

    def owlapi_is_functional_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_functional|', property_, reasoner)

    def owlapi_is_inverse_functional(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_inverse_functional|', property_, reasoner))

    def owlapi_is_inverse_functional_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_inverse_functional|', property_, reasoner)

    def owlapi_is_irreflexive(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_irreflexive|', property_, reasoner))

    def owlapi_is_irreflexive_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_irreflexive|', property_, reasoner)

    def owlapi_is_realised(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_realised|', reasoner))

    def owlapi_is_realised_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_realised|', reasoner)

    def owlapi_is_reflexive(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_reflexive|', property_, reasoner))

    def owlapi_is_reflexive_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_reflexive|', property_, reasoner)

    def owlapi_is_same_individual(self, i=None, j=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_same_individual|', i, j, reasoner))

    def owlapi_is_same_individual_(self, i=None, j=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_same_individual|', i, j, reasoner)

    def owlapi_is_satisfiable(self, description=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_satisfiable|', description, reasoner))

    def owlapi_is_satisfiable_(self, description=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_satisfiable|', description, reasoner)

    def owlapi_is_sub_class_of(self, clsc=None, clsd=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_sub_class_of|', clsc, clsd, reasoner))

    def owlapi_is_sub_class_of_(self, clsc=None, clsd=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_sub_class_of|', clsc, clsd, reasoner)

    def owlapi_is_symmetric(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_symmetric|', property_, reasoner))

    def owlapi_is_symmetric_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_symmetric|', property_, reasoner)

    def owlapi_is_transitive(self, property_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-is_transitive|', property_, reasoner))

    def owlapi_is_transitive_(self, property_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-is_transitive|', property_, reasoner)

    def owlapi_keep_annotations(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-keep_annotations|', reasoner))

    def owlapi_keep_annotations_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-keep_annotations|', reasoner)

    def owlapi_load_axiom(self, ont=None, axiom=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-load_axiom|', ont, axiom, reasoner))

    def owlapi_load_axiom_(self, ont=None, axiom=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-load_axiom|', ont, axiom, reasoner)

    def owlapi_load_axioms(self, ont=None, axioms=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-load_axioms|', ont, axioms, reasoner))

    def owlapi_load_axioms_(self, ont=None, axioms=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-load_axioms|', ont, axioms, reasoner)

    def owlapi_load_ontologies(self, ontologies=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-load_ontologies|', ontologies, reasoner))

    def owlapi_load_ontologies_(self, ontologies=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-load_ontologies|', ontologies, reasoner)

    def owlapi_load_ontology(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-load_ontology|', ontology, reasoner))

    def owlapi_load_ontology_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-load_ontology|', ontology, reasoner)

    def owlapi_manually_apply_changes(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-manually_apply_changes|', reasoner))

    def owlapi_manually_apply_changes_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-manually_apply_changes|', reasoner)

    def owlapi_merge_ontologies(self, ont1=None, ont2=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-merge_ontologies|', ont1, ont2, reasoner))

    def owlapi_merge_ontologies_(self, ont1=None, ont2=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-merge_ontologies|', ont1, ont2, reasoner)

    def owlapi_new_ontology(self, name=None, reasoner=None, secondary_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-new_ontology|', name, reasoner, secondary_p))

    def owlapi_new_ontology_(self, name=None, reasoner=None, secondary_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-new_ontology|', name, reasoner, secondary_p)

    def owlapi_new_reasoner(self, owlapi_reasoner_name=None, make_racer_kb_current_p=None, init=None, owlapi_tbox=None, owlapi_abox=None, own_racer_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-new_reasoner|', owlapi_reasoner_name, make_racer_kb_current_p, init, owlapi_tbox, owlapi_abox, own_racer_p))

    def owlapi_new_reasoner_(self, owlapi_reasoner_name=None, make_racer_kb_current_p=None, init=None, owlapi_tbox=None, owlapi_abox=None, own_racer_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-new_reasoner|', owlapi_reasoner_name, make_racer_kb_current_p, init, owlapi_tbox, owlapi_abox, own_racer_p)

    def owlapi_new_reasoner1(self, owlapi_reasoner_name=None, make_racer_kb_current_p=None, init=None, owlapi_tbox=None, owlapi_abox=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-new_reasoner1|', owlapi_reasoner_name, make_racer_kb_current_p, init, owlapi_tbox, owlapi_abox))

    def owlapi_new_reasoner1_(self, owlapi_reasoner_name=None, make_racer_kb_current_p=None, init=None, owlapi_tbox=None, owlapi_abox=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-new_reasoner1|', owlapi_reasoner_name, make_racer_kb_current_p, init, owlapi_tbox, owlapi_abox)

    def owlapi_next_axiom_use_i_d(self, id=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-next_axiom_use_i_d|', id, reasoner))

    def owlapi_next_axiom_use_i_d_(self, id=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-next_axiom_use_i_d|', id, reasoner)

    def owlapi_parse_native(self, string=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-parse_native|', string, reasoner))

    def owlapi_parse_native_(self, string=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-parse_native|', string, reasoner)

    def owlapi_read_functional_ontology_document(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-read_functional_ontology_document|', key_args))

    def owlapi_read_functional_ontology_document_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-read_functional_ontology_document|', key_args)

    def owlapi_read_functional_ontology_file(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-read_functional_ontology_file|', key_args))

    def owlapi_read_functional_ontology_file_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-read_functional_ontology_file|', key_args)

    def owlapi_read_ontology(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-read_ontology|', key_args))

    def owlapi_read_ontology_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-read_ontology|', key_args)

    def owlapi_read_x_m_l_ontology_document(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-read_x_m_l_ontology_document|', key_args))

    def owlapi_read_x_m_l_ontology_document_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-read_x_m_l_ontology_document|', key_args)

    def owlapi_read_x_m_l_ontology_file(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-read_x_m_l_ontology_file|', key_args))

    def owlapi_read_x_m_l_ontology_file_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-read_x_m_l_ontology_file|', key_args)

    def owlapi_register_declared_entities(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-register_declared_entities|', reasoner))

    def owlapi_register_declared_entities_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-register_declared_entities|', reasoner)

    def owlapi_register_last_answer(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-register_last_answer|', reasoner))

    def owlapi_register_last_answer_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-register_last_answer|', reasoner)

    def owlapi_register_object(self, obj=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-register_object|', obj))

    def owlapi_register_object_(self, obj=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-register_object|', obj)

    def owlapi_register_referenced_entities(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-register_referenced_entities|', reasoner))

    def owlapi_register_referenced_entities_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-register_referenced_entities|', reasoner)

    def owlapi_reload_loaded_ontologies(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-reload_loaded_ontologies|', reasoner))

    def owlapi_reload_loaded_ontologies_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-reload_loaded_ontologies|', reasoner)

    def owlapi_remove_axiom(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-remove_axiom|'))

    def owlapi_remove_axiom_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-remove_axiom|')

    def owlapi_remove_axioms(self) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-remove_axioms|'))

    def owlapi_remove_axioms_(self) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-remove_axioms|')

    def owlapi_remove_prefix(self, prefix=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-remove_prefix|', prefix, reasoner))

    def owlapi_remove_prefix_(self, prefix=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-remove_prefix|', prefix, reasoner)

    def owlapi_reset_axiom_counter(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-reset_axiom_counter|', reasoner))

    def owlapi_reset_axiom_counter_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-reset_axiom_counter|', reasoner)

    def owlapi_restore_image(self, fn=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-restore_image|', fn))

    def owlapi_restore_image_(self, fn=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-restore_image|', fn)

    def owlapi_save_ontology(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-save_ontology|', key_args))

    def owlapi_save_ontology_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-save_ontology|', key_args)

    def owlapi_set_auto_declare_data_properties(self, val=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-set_auto_declare_data_properties|', val, reasoner))

    def owlapi_set_auto_declare_data_properties_(self, val=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-set_auto_declare_data_properties|', val, reasoner)

    def owlapi_set_axiom_counter(self, n=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-set_axiom_counter|', n, reasoner))

    def owlapi_set_axiom_counter_(self, n=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-set_axiom_counter|', n, reasoner)

    def owlapi_set_current_reasoner(self, name=None, make_racer_kb_current_p=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-set_current_reasoner|', name, make_racer_kb_current_p))

    def owlapi_set_current_reasoner_(self, name=None, make_racer_kb_current_p=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-set_current_reasoner|', name, make_racer_kb_current_p)

    def owlapi_set_ontology_u_r_i(self, ont=None, uri=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-_set_ontology_u_r_i|', ont, uri, reasoner))

    def owlapi_set_ontology_u_r_i_(self, ont=None, uri=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-_set_ontology_u_r_i|', ont, uri, reasoner)

    def owlapi_set_progress(self, n=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-set_progress|', n, reasoner))

    def owlapi_set_progress_(self, n=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-set_progress|', n, reasoner)

    def owlapi_set_progress_range(self, steps=None, from_=None, to=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-set_progress_range|', steps, from_, to, reasoner))

    def owlapi_set_progress_range_(self, steps=None, from_=None, to=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-set_progress_range|', steps, from_, to, reasoner)

    def owlapi_set_return_policy(self, type_=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-set_return_policy|', type_, reasoner))

    def owlapi_set_return_policy_(self, type_=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-set_return_policy|', type_, reasoner)

    def owlapi_store_image(self, fn=None, reasoners=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-store_image|', fn, reasoners))

    def owlapi_store_image_(self, fn=None, reasoners=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-store_image|', fn, reasoners)

    def owlapi_unload_axiom(self, ont=None, axiom=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-unload_axiom|', ont, axiom, reasoner))

    def owlapi_unload_axiom_(self, ont=None, axiom=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-unload_axiom|', ont, axiom, reasoner)

    def owlapi_unload_axioms(self, ont=None, axioms=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-unload_axioms|', ont, axioms, reasoner))

    def owlapi_unload_axioms_(self, ont=None, axioms=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-unload_axioms|', ont, axioms, reasoner)

    def owlapi_unload_ontologies(self, ontologies=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-unload_ontologies|', ontologies, reasoner))

    def owlapi_unload_ontologies_(self, ontologies=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-unload_ontologies|', ontologies, reasoner)

    def owlapi_unload_ontology(self, ontology=None, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-unload_ontology|', ontology, reasoner))

    def owlapi_unload_ontology_(self, ontology=None, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-unload_ontology|', ontology, reasoner)

    def owlapi_uses_incremental_updates(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-uses_incremental_updates|', reasoner))

    def owlapi_uses_incremental_updates_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-uses_incremental_updates|', reasoner)

    def owlapi_uses_simplified_protocol(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-uses_simplified_protocol|', reasoner))

    def owlapi_uses_simplified_protocol_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-uses_simplified_protocol|', reasoner)

    def owlapi_write_functional_ontology_file(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-write_functional_ontology_file|', key_args))

    def owlapi_write_functional_ontology_file_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-write_functional_ontology_file|', key_args)

    def owlapi_write_ontology_file(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-write_ontology_file|', key_args))

    def owlapi_write_ontology_file_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-write_ontology_file|', key_args)

    def owlapi_write_x_m_l_ontology_file(self, *key_args) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-write_x_m_l_ontology_file|', key_args))

    def owlapi_write_x_m_l_ontology_file_(self, *key_args) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-write_x_m_l_ontology_file|', key_args)

    def owllink_read_document(self, *key_args) -> str:
        return str(self.racer_call('owllink-read-document', key_args))

    def owllink_read_document_(self, *key_args) -> RacerResult:
        return self.racer_call('owllink-read-document', key_args)

    def owllink_read_file(self, *key_args) -> str:
        return str(self.racer_call('owllink-read-file', key_args))

    def owllink_read_file_(self, *key_args) -> RacerResult:
        return self.racer_call('owllink-read-file', key_args)

    def pracer_answer_query(self, *key_args) -> str:
        return str(self.racer_call('pracer-answer-query', key_args))

    def pracer_answer_query_(self, *key_args) -> RacerResult:
        return self.racer_call('pracer-answer-query', key_args)

    def prefer_defined_queries(self) -> str:
        return str(self.racer_call('prefer-defined-queries'))

    def prefer_defined_queries_(self) -> RacerResult:
        return self.racer_call('prefer-defined-queries')

    def prepare_abox(self, abox=None) -> str:
        return str(self.racer_call('prepare-abox', abox))

    def prepare_abox_(self, abox=None) -> RacerResult:
        return self.racer_call('prepare-abox', abox)

    def prepare_nrql_engine(self, *key_args) -> str:
        return str(self.racer_call('prepare-nrql-engine', key_args))

    def prepare_nrql_engine_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-nrql-engine', key_args)

    def prepare_query(self, *key_args) -> str:
        return str(self.racer_call('prepare-query', key_args))

    def prepare_query_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-query', key_args)

    def prepare_query1(self, *key_args) -> str:
        return str(self.racer_call('prepare-query1', key_args))

    def prepare_query1_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-query1', key_args)

    def prepare_racer_engine(self, *key_args) -> str:
        return str(self.racer_call('prepare-racer-engine', key_args))

    def prepare_racer_engine_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-racer-engine', key_args)

    def prepare_rule(self, *key_args) -> str:
        return str(self.racer_call('prepare-rule', key_args))

    def prepare_rule_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-rule', key_args)

    def prepare_rule1(self, *key_args) -> str:
        return str(self.racer_call('prepare-rule1', key_args))

    def prepare_rule1_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-rule1', key_args)

    def prepared_queries(self, *key_args) -> str:
        return str(self.racer_call('prepared-queries', key_args))

    def prepared_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('prepared-queries', key_args)

    def prepared_rules(self, *key_args) -> str:
        return str(self.racer_call('prepared-rules', key_args))

    def prepared_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('prepared-rules', key_args)

    def print_abox_individuals(self, *key_args) -> str:
        return str(self.racer_call('print-abox-individuals', key_args))

    def print_abox_individuals_(self, *key_args) -> RacerResult:
        return self.racer_call('print-abox-individuals', key_args)

    def print_tbox_tree(self, tbox=None, stream=None, hide_role_inverses=None) -> str:
        return str(self.racer_call('print-tbox-tree', tbox, stream, hide_role_inverses))

    def print_tbox_tree_(self, tbox=None, stream=None, hide_role_inverses=None) -> RacerResult:
        return self.racer_call('print-tbox-tree', tbox, stream, hide_role_inverses)

    def process_set_at_a_time(self) -> str:
        return str(self.racer_call('process-set-at-a-time'))

    def process_set_at_a_time_(self) -> RacerResult:
        return self.racer_call('process-set-at-a-time')

    def process_tuple_at_a_time(self) -> str:
        return str(self.racer_call('process-tuple-at-a-time'))

    def process_tuple_at_a_time_(self) -> RacerResult:
        return self.racer_call('process-tuple-at-a-time')

    def processed_queries(self, *key_args) -> str:
        return str(self.racer_call('processed-queries', key_args))

    def processed_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('processed-queries', key_args)

    def processed_rules(self, *key_args) -> str:
        return str(self.racer_call('processed-rules', key_args))

    def processed_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('processed-rules', key_args)

    def publish1(self, individual=None, abox=None) -> str:
        return str(self.racer_call('publish-1', individual, abox))

    def publish1_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('publish-1', individual, abox)

    def publish_file(self, filename=None, url=None, content_type=None) -> str:
        return str(self.racer_call('publish-file', filename, url, content_type))

    def publish_file_(self, filename=None, url=None, content_type=None) -> RacerResult:
        return self.racer_call('publish-file', filename, url, content_type)

    def query_accurate_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-accurate-p', query))

    def query_active_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-active-p', query))

    def query_ancestors(self, query=None) -> str:
        return str(self.racer_call('query-ancestors', query))

    def query_ancestors_(self, query=None) -> RacerResult:
        return self.racer_call('query-ancestors', query)

    def query_body(self, query=None) -> str:
        return str(self.racer_call('query-body', query))

    def query_body_(self, query=None) -> RacerResult:
        return self.racer_call('query-body', query)

    def query_children(self, query=None) -> str:
        return str(self.racer_call('query-children', query))

    def query_children_(self, query=None) -> RacerResult:
        return self.racer_call('query-children', query)

    def query_consistent_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-consistent-p', query))

    def query_descendants(self, query=None) -> str:
        return str(self.racer_call('query-descendants', query))

    def query_descendants_(self, query=None) -> RacerResult:
        return self.racer_call('query-descendants', query)

    def query_entails_p(self, a=None, b=None) -> bool:
        return self.return_boolean(self.racer_call('query-entails-p', a, b))

    def query_equivalent_p(self, a=None, b=None) -> bool:
        return self.return_boolean(self.racer_call('query-equivalent-p', a, b))

    def query_equivalents(self, query=None) -> str:
        return str(self.racer_call('query-equivalents', query))

    def query_equivalents_(self, query=None) -> RacerResult:
        return self.racer_call('query-equivalents', query)

    def query_head(self, query=None) -> str:
        return str(self.racer_call('query-head', query))

    def query_head_(self, query=None) -> RacerResult:
        return self.racer_call('query-head', query)

    def query_parents(self, query=None) -> str:
        return str(self.racer_call('query-parents', query))

    def query_parents_(self, query=None) -> RacerResult:
        return self.racer_call('query-parents', query)

    def query_prepared_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-prepared-p', query))

    def query_processed_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-processed-p', query))

    def query_ready_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-ready-p', query))

    def query_running_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-running-p', query))

    def query_sleeping_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-sleeping-p', query))

    def query_subscribers(self, query=None) -> str:
        return str(self.racer_call('query-subscribers', query))

    def query_subscribers_(self, query=None) -> RacerResult:
        return self.racer_call('query-subscribers', query)

    def query_terminated_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-terminated-p', query))

    def query_waiting_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('query-waiting-p', query))

    def racer_answer_query(self, *key_args) -> str:
        return str(self.racer_call('racer-answer-query', key_args))

    def racer_answer_query_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-answer-query', key_args)

    def racer_answer_query_under_premise(self, *key_args) -> str:
        return str(self.racer_call('racer-answer-query-under-premise', key_args))

    def racer_answer_query_under_premise_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-answer-query-under-premise', key_args)

    def racer_answer_query_under_premise1(self, *key_args) -> str:
        return str(self.racer_call('racer-answer-query-under-premise1', key_args))

    def racer_answer_query_under_premise1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-answer-query-under-premise1', key_args)

    def racer_answer_query_with_explanation(self, *key_args) -> str:
        return str(self.racer_call('racer-answer-query-with-explanation', key_args))

    def racer_answer_query_with_explanation_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-answer-query-with-explanation', key_args)

    def racer_answer_query1(self, *key_args) -> str:
        return str(self.racer_call('racer-answer-query1', key_args))

    def racer_answer_query1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-answer-query1', key_args)

    def racer_answer_tbox_query(self, *key_args) -> str:
        return str(self.racer_call('racer-answer-tbox-query', key_args))

    def racer_answer_tbox_query_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-answer-tbox-query', key_args)

    def racer_answer_tbox_query1(self, *key_args) -> str:
        return str(self.racer_call('racer-answer-tbox-query1', key_args))

    def racer_answer_tbox_query1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-answer-tbox-query1', key_args)

    def racer_apply_rule(self, *key_args) -> str:
        return str(self.racer_call('racer-apply-rule', key_args))

    def racer_apply_rule_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-apply-rule', key_args)

    def racer_apply_rule_under_premise(self, *key_args) -> str:
        return str(self.racer_call('racer-apply-rule-under-premise', key_args))

    def racer_apply_rule_under_premise_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-apply-rule-under-premise', key_args)

    def racer_apply_rule_under_premise1(self, *key_args) -> str:
        return str(self.racer_call('racer-apply-rule-under-premise1', key_args))

    def racer_apply_rule_under_premise1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-apply-rule-under-premise1', key_args)

    def racer_apply_rule1(self, *key_args) -> str:
        return str(self.racer_call('racer-apply-rule1', key_args))

    def racer_apply_rule1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-apply-rule1', key_args)

    def racer_prepare_query(self, *key_args) -> str:
        return str(self.racer_call('racer-prepare-query', key_args))

    def racer_prepare_query_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-prepare-query', key_args)

    def racer_prepare_query1(self, *key_args) -> str:
        return str(self.racer_call('racer-prepare-query1', key_args))

    def racer_prepare_query1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-prepare-query1', key_args)

    def racer_prepare_rule(self, *key_args) -> str:
        return str(self.racer_call('racer-prepare-rule', key_args))

    def racer_prepare_rule_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-prepare-rule', key_args)

    def racer_prepare_rule1(self, *key_args) -> str:
        return str(self.racer_call('racer-prepare-rule1', key_args))

    def racer_prepare_rule1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-prepare-rule1', key_args)

    def racer_prepare_tbox_query(self, *key_args) -> str:
        return str(self.racer_call('racer-prepare-tbox-query', key_args))

    def racer_prepare_tbox_query_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-prepare-tbox-query', key_args)

    def racer_prepare_tbox_query1(self, *key_args) -> str:
        return str(self.racer_call('racer-prepare-tbox-query1', key_args))

    def racer_prepare_tbox_query1_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-prepare-tbox-query1', key_args)

    def racer_read_document(self, *key_args) -> str:
        return str(self.racer_call('racer-read-document', key_args))

    def racer_read_document_(self, *key_args) -> RacerResult:
        return self.racer_call('racer-read-document', key_args)

    def racer_read_file(self, filename=None) -> str:
        return str(self.racer_call('racer-read-file', filename))

    def racer_read_file_(self, filename=None) -> RacerResult:
        return self.racer_call('racer-read-file', filename)

    def rcc_consistent_p(self, abox=None, type_of_substrate=None) -> bool:
        return self.return_boolean(self.racer_call('rcc-consistent-p', abox, type_of_substrate))

    def rcc_edge_description1(self) -> str:
        return str(self.racer_call('rcc-edge-description1'))

    def rcc_edge_description1_(self) -> RacerResult:
        return self.racer_call('rcc-edge-description1')

    def rcc_edge_label1(self) -> str:
        return str(self.racer_call('rcc-edge-label1'))

    def rcc_edge_label1_(self) -> RacerResult:
        return self.racer_call('rcc-edge-label1')

    def rcc_edge1(self) -> str:
        return str(self.racer_call('rcc-edge1'))

    def rcc_edge1_(self) -> RacerResult:
        return self.racer_call('rcc-edge1')

    def rcc_instance1(self) -> str:
        return str(self.racer_call('rcc-instance1'))

    def rcc_instance1_(self) -> RacerResult:
        return self.racer_call('rcc-instance1')

    def rcc_node_description1(self) -> str:
        return str(self.racer_call('rcc-node-description1'))

    def rcc_node_description1_(self) -> RacerResult:
        return self.racer_call('rcc-node-description1')

    def rcc_node_label1(self) -> str:
        return str(self.racer_call('rcc-node-label1'))

    def rcc_node_label1_(self) -> RacerResult:
        return self.racer_call('rcc-node-label1')

    def rcc_node1(self) -> str:
        return str(self.racer_call('rcc-node1'))

    def rcc_node1_(self) -> RacerResult:
        return self.racer_call('rcc-node1')

    def rcc_related1(self) -> str:
        return str(self.racer_call('rcc-related1'))

    def rcc_related1_(self) -> RacerResult:
        return self.racer_call('rcc-related1')

    def rdfs_read_tbox_file(self, filename=None) -> str:
        return str(self.racer_call('rdfs-read-tbox-file', filename))

    def rdfs_read_tbox_file_(self, filename=None) -> RacerResult:
        return self.racer_call('rdfs-read-tbox-file', filename)

    def ready_queries(self, *key_args) -> str:
        return str(self.racer_call('ready-queries', key_args))

    def ready_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('ready-queries', key_args)

    def ready_rules(self, *key_args) -> str:
        return str(self.racer_call('ready-rules', key_args))

    def ready_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('ready-rules', key_args)

    def realize_abox(self, abox=None, individual_name=None) -> str:
        return str(self.racer_call('realize-abox', abox, individual_name))

    def realize_abox_(self, abox=None, individual_name=None) -> RacerResult:
        return self.racer_call('realize-abox', abox, individual_name)

    def recognize_events(self, abox=None) -> str:
        return str(self.racer_call('recognize-events', abox))

    def recognize_events_(self, abox=None) -> RacerResult:
        return self.racer_call('recognize-events', abox)

    def reexecute_all_queries(self, *key_args) -> str:
        return str(self.racer_call('reexecute-all-queries', key_args))

    def reexecute_all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('reexecute-all-queries', key_args)

    def reexecute_all_rules(self, *key_args) -> str:
        return str(self.racer_call('reexecute-all-rules', key_args))

    def reexecute_all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('reexecute-all-rules', key_args)

    def reexecute_query(self, query=None) -> str:
        return str(self.racer_call('reexecute-query', query))

    def reexecute_query_(self, query=None) -> RacerResult:
        return self.racer_call('reexecute-query', query)

    def reexecute_rule(self, query=None) -> str:
        return str(self.racer_call('reexecute-rule', query))

    def reexecute_rule_(self, query=None) -> RacerResult:
        return self.racer_call('reexecute-rule', query)

    def reflexive_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('reflexive-p', role_term, tbox))

    def register_rcc_synonym(self, role=None, rcc_relation=None) -> str:
        return str(self.racer_call('register-rcc-synonym', role, rcc_relation))

    def register_rcc_synonym_(self, role=None, rcc_relation=None) -> RacerResult:
        return self.racer_call('register-rcc-synonym', role, rcc_relation)

    def remove_implied_concept_assertions(self, abox=None) -> str:
        return str(self.racer_call('remove-implied-concept-assertions', abox))

    def remove_implied_concept_assertions_(self, abox=None) -> RacerResult:
        return self.racer_call('remove-implied-concept-assertions', abox)

    def report_inconsistent_queries_and_rules(self) -> str:
        return str(self.racer_call('report-inconsistent-queries-and-rules'))

    def report_inconsistent_queries_and_rules_(self) -> RacerResult:
        return self.racer_call('report-inconsistent-queries-and-rules')

    def reprepare_query(self, *key_args) -> str:
        return str(self.racer_call('reprepare-query', key_args))

    def reprepare_query_(self, *key_args) -> RacerResult:
        return self.racer_call('reprepare-query', key_args)

    def reprepare_rule(self, query=None) -> str:
        return str(self.racer_call('reprepare-rule', query))

    def reprepare_rule_(self, query=None) -> RacerResult:
        return self.racer_call('reprepare-rule', query)

    def reset_all_substrates(self, *key_args) -> str:
        return str(self.racer_call('reset-all-substrates', key_args))

    def reset_all_substrates_(self, *key_args) -> RacerResult:
        return self.racer_call('reset-all-substrates', key_args)

    def reset_nrql_engine(self, *key_args) -> str:
        return str(self.racer_call('reset-nrql-engine', key_args))

    def reset_nrql_engine_(self, *key_args) -> RacerResult:
        return self.racer_call('reset-nrql-engine', key_args)

    def restore_abox_image(self, filename=None) -> str:
        return str(self.racer_call('restore-abox-image', filename))

    def restore_abox_image_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-abox-image', filename)

    def restore_aboxes_image(self, filename=None) -> str:
        return str(self.racer_call('restore-aboxes-image', filename))

    def restore_aboxes_image_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-aboxes-image', filename)

    def restore_all_substrates(self, filename=None) -> str:
        return str(self.racer_call('restore-all-substrates', filename))

    def restore_all_substrates_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-all-substrates', filename)

    def restore_kb_image(self, filename=None) -> str:
        return str(self.racer_call('restore-kb-image', filename))

    def restore_kb_image_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-kb-image', filename)

    def restore_kbs_image(self, filename=None) -> str:
        return str(self.racer_call('restore-kbs-image', filename))

    def restore_kbs_image_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-kbs-image', filename)

    def restore_server_image(self, filename=None) -> str:
        return str(self.racer_call('restore-server-image', filename))

    def restore_server_image_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-server-image', filename)

    def restore_standard_settings(self) -> str:
        return str(self.racer_call('restore-standard-settings'))

    def restore_standard_settings_(self) -> RacerResult:
        return self.racer_call('restore-standard-settings')

    def restore_substrate(self, filename=None) -> str:
        return str(self.racer_call('restore-substrate', filename))

    def restore_substrate_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-substrate', filename)

    def restore_tbox_image(self, filename=None) -> str:
        return str(self.racer_call('restore-tbox-image', filename))

    def restore_tbox_image_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-tbox-image', filename)

    def restore_tboxes_image(self, filename=None) -> str:
        return str(self.racer_call('restore-tboxes-image', filename))

    def restore_tboxes_image_(self, filename=None) -> RacerResult:
        return self.racer_call('restore-tboxes-image', filename)

    def retrieve_concept_instances(self, concept_term=None, abox=None, candidates=None) -> str:
        return str(self.racer_call('retrieve-concept-instances', concept_term, abox, candidates))

    def retrieve_concept_instances_(self, concept_term=None, abox=None, candidates=None) -> RacerResult:
        return self.racer_call('retrieve-concept-instances', concept_term, abox, candidates)

    def retrieve_direct_predecessors(self, role_term=None, ind_filler=None, abox=None) -> str:
        return str(self.racer_call('retrieve-direct-predecessors', role_term, ind_filler, abox))

    def retrieve_direct_predecessors_(self, role_term=None, ind_filler=None, abox=None) -> RacerResult:
        return self.racer_call('retrieve-direct-predecessors', role_term, ind_filler, abox)

    def retrieve_individual_annotation_property_fillers(self, individual_name=None, role=None, abox=None, with_types_p=None) -> str:
        return str(self.racer_call('retrieve-individual-annotation-property-fillers', individual_name, role, abox, with_types_p))

    def retrieve_individual_annotation_property_fillers_(self, individual_name=None, role=None, abox=None, with_types_p=None) -> RacerResult:
        return self.racer_call('retrieve-individual-annotation-property-fillers', individual_name, role, abox, with_types_p)

    def retrieve_individual_antonyms(self, individual=None, told_only=None, abox=None) -> str:
        return str(self.racer_call('retrieve-individual-antonyms', individual, told_only, abox))

    def retrieve_individual_antonyms_(self, individual=None, told_only=None, abox=None) -> RacerResult:
        return self.racer_call('retrieve-individual-antonyms', individual, told_only, abox)

    def retrieve_individual_attribute_fillers(self, ind=None, attribute=None, abox=None) -> str:
        return str(self.racer_call('retrieve-individual-attribute-fillers', ind, attribute, abox))

    def retrieve_individual_attribute_fillers_(self, ind=None, attribute=None, abox=None) -> RacerResult:
        return self.racer_call('retrieve-individual-attribute-fillers', ind, attribute, abox)

    def retrieve_individual_filled_roles(self, *key_args) -> str:
        return str(self.racer_call('retrieve-individual-filled-roles', key_args))

    def retrieve_individual_filled_roles_(self, *key_args) -> RacerResult:
        return self.racer_call('retrieve-individual-filled-roles', key_args)

    def retrieve_individual_fillers(self, ind_predecessor=None, role_term=None, abox=None) -> str:
        return str(self.racer_call('retrieve-individual-fillers', ind_predecessor, role_term, abox))

    def retrieve_individual_fillers_(self, ind_predecessor=None, role_term=None, abox=None) -> RacerResult:
        return self.racer_call('retrieve-individual-fillers', ind_predecessor, role_term, abox)

    def retrieve_individual_synonyms(self, individual=None, told_only=None, abox=None) -> str:
        return str(self.racer_call('retrieve-individual-synonyms', individual, told_only, abox))

    def retrieve_individual_synonyms_(self, individual=None, told_only=None, abox=None) -> RacerResult:
        return self.racer_call('retrieve-individual-synonyms', individual, told_only, abox)

    def retrieve_individual_told_attribute_value(self, ind=None, attribute=None, abox=None) -> str:
        return str(self.racer_call('retrieve-individual-told-attribute-value', ind, attribute, abox))

    def retrieve_individual_told_attribute_value_(self, ind=None, attribute=None, abox=None) -> RacerResult:
        return self.racer_call('retrieve-individual-told-attribute-value', ind, attribute, abox)

    def retrieve_individual_told_datatype_fillers(self, ind=None, datatype_role=None, direct_p=None, abox=None, with_types_p=None) -> str:
        return str(self.racer_call('retrieve-individual-told-datatype-fillers', ind, datatype_role, direct_p, abox, with_types_p))

    def retrieve_individual_told_datatype_fillers_(self, ind=None, datatype_role=None, direct_p=None, abox=None, with_types_p=None) -> RacerResult:
        return self.racer_call('retrieve-individual-told-datatype-fillers', ind, datatype_role, direct_p, abox, with_types_p)

    def retrieve_related_individuals(self, role_term=None, abox=None) -> str:
        return str(self.racer_call('retrieve-related-individuals', role_term, abox))

    def retrieve_related_individuals_(self, role_term=None, abox=None) -> RacerResult:
        return self.racer_call('retrieve-related-individuals', role_term, abox)

    def rmi(self, args=None) -> str:
        return str(self.racer_call('rmi', args))

    def rmi_(self, args=None) -> RacerResult:
        return self.racer_call('rmi', args)

    def role_disjoint_p(self, role_term1=None, role_term2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-disjoint-p', role_term1, role_term2, tbox))

    def role_equivalent_p(self, role1=None, role2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-equivalent-p', role1, role2, tbox))

    def role_has_domain(self, rolename=None, concept=None, tbox=None, errorp=None) -> str:
        return str(self.racer_call('role-has-domain', rolename, concept, tbox, errorp))

    def role_has_domain_(self, rolename=None, concept=None, tbox=None, errorp=None) -> RacerResult:
        return self.racer_call('role-has-domain', rolename, concept, tbox, errorp)

    def role_has_parent(self, rolename1=None, rolename2=None, tbox=None) -> str:
        return str(self.racer_call('role-has-parent', rolename1, rolename2, tbox))

    def role_has_parent_(self, rolename1=None, rolename2=None, tbox=None) -> RacerResult:
        return self.racer_call('role-has-parent', rolename1, rolename2, tbox)

    def role_has_range(self, rolename=None, concept=None, tbox=None, errorp=None) -> str:
        return str(self.racer_call('role-has-range', rolename, concept, tbox, errorp))

    def role_has_range_(self, rolename=None, concept=None, tbox=None, errorp=None) -> RacerResult:
        return self.racer_call('role-has-range', rolename, concept, tbox, errorp)

    def role_is_asymmetric(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-asymmetric', rolename, tbox))

    def role_is_asymmetric_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-asymmetric', rolename, tbox)

    def role_is_functional(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-functional', rolename, tbox))

    def role_is_functional_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-functional', rolename, tbox)

    def role_is_irreflexive(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-irreflexive', rolename, tbox))

    def role_is_irreflexive_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-irreflexive', rolename, tbox)

    def role_is_reflexive(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-reflexive', rolename, tbox))

    def role_is_reflexive_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-reflexive', rolename, tbox)

    def role_is_symmetric(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-symmetric', rolename, tbox))

    def role_is_symmetric_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-symmetric', rolename, tbox)

    def role_is_transitive(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-transitive', rolename, tbox))

    def role_is_transitive_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-transitive', rolename, tbox)

    def role_is_used_as_annotation_property(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-used-as-annotation-property', rolename, tbox))

    def role_is_used_as_annotation_property_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-used-as-annotation-property', rolename, tbox)

    def role_is_used_as_datatype_property(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('role-is-used-as-datatype-property', rolename, tbox))

    def role_is_used_as_datatype_property_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('role-is-used-as-datatype-property', rolename, tbox)

    def role_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-p', role_term, tbox))

    def role_satisfiable_p(self, role=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-satisfiable-p', role, tbox))

    def role_subsumes_p(self, role_term1=None, role_term2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-subsumes-p', role_term1, role_term2, tbox))

    def role_used_as_annotation_property_p(self, role_name=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-used-as-annotation-property-p', role_name, tbox))

    def role_used_as_datatype_property_p(self, role_name=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-used-as-datatype-property-p', role_name, tbox))

    def roles_disjoint1(self, role1=None, role2=None, tbox=None) -> str:
        return str(self.racer_call('roles-disjoint-1', role1, role2, tbox))

    def roles_disjoint1_(self, role1=None, role2=None, tbox=None) -> RacerResult:
        return self.racer_call('roles-disjoint-1', role1, role2, tbox)

    def roles_equivalent1(self, role1=None, role2=None, tbox=None) -> str:
        return str(self.racer_call('roles-equivalent-1', role1, role2, tbox))

    def roles_equivalent1_(self, role1=None, role2=None, tbox=None) -> RacerResult:
        return self.racer_call('roles-equivalent-1', role1, role2, tbox)

    def rule_accurate_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-accurate-p', query))

    def rule_active_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-active-p', query))

    def rule_antecedence(self, query=None) -> str:
        return str(self.racer_call('rule-antecedence', query))

    def rule_antecedence_(self, query=None) -> RacerResult:
        return self.racer_call('rule-antecedence', query)

    def rule_applicable_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-applicable-p', query))

    def rule_consequence(self, query=None) -> str:
        return str(self.racer_call('rule-consequence', query))

    def rule_consequence_(self, query=None) -> RacerResult:
        return self.racer_call('rule-consequence', query)

    def rule_consistent_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-consistent-p', query))

    def rule_prepared_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-prepared-p', query))

    def rule_processed_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-processed-p', query))

    def rule_ready_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-ready-p', query))

    def rule_running_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-running-p', query))

    def rule_sleeping_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-sleeping-p', query))

    def rule_terminated_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-terminated-p', query))

    def rule_unapplicable_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-unapplicable-p', query))

    def rule_waiting_p(self, query=None) -> bool:
        return self.return_boolean(self.racer_call('rule-waiting-p', query))

    def run_all_queries(self, *key_args) -> str:
        return str(self.racer_call('run-all-queries', key_args))

    def run_all_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('run-all-queries', key_args)

    def run_all_rules(self, *key_args) -> str:
        return str(self.racer_call('run-all-rules', key_args))

    def run_all_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('run-all-rules', key_args)

    def running_cheap_queries(self, *key_args) -> str:
        return str(self.racer_call('running-cheap-queries', key_args))

    def running_cheap_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('running-cheap-queries', key_args)

    def running_cheap_rules(self, *key_args) -> str:
        return str(self.racer_call('running-cheap-rules', key_args))

    def running_cheap_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('running-cheap-rules', key_args)

    def running_expensive_queries(self, *key_args) -> str:
        return str(self.racer_call('running-expensive-queries', key_args))

    def running_expensive_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('running-expensive-queries', key_args)

    def running_expensive_rules(self, *key_args) -> str:
        return str(self.racer_call('running-expensive-rules', key_args))

    def running_expensive_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('running-expensive-rules', key_args)

    def running_queries(self, *key_args) -> str:
        return str(self.racer_call('running-queries', key_args))

    def running_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('running-queries', key_args)

    def running_rules(self, *key_args) -> str:
        return str(self.racer_call('running-rules', key_args))

    def running_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('running-rules', key_args)

    def save_abox(self, *key_args) -> str:
        return str(self.racer_call('save-abox', key_args))

    def save_abox_(self, *key_args) -> RacerResult:
        return self.racer_call('save-abox', key_args)

    def save_kb(self, *key_args) -> str:
        return str(self.racer_call('save-kb', key_args))

    def save_kb_(self, *key_args) -> RacerResult:
        return self.racer_call('save-kb', key_args)

    def save_ontology_to_triple_store(self, *key_args) -> str:
        return str(self.racer_call('save-ontology-to-triple-store', key_args))

    def save_ontology_to_triple_store_(self, *key_args) -> RacerResult:
        return self.racer_call('save-ontology-to-triple-store', key_args)

    def save_tbox(self, *key_args) -> str:
        return str(self.racer_call('save-tbox', key_args))

    def save_tbox_(self, *key_args) -> RacerResult:
        return self.racer_call('save-tbox', key_args)

    def server_case(self) -> str:
        return str(self.racer_call('server-case'))

    def server_case_(self) -> RacerResult:
        return self.racer_call('server-case')

    def server_function(self, name=None) -> str:
        return str(self.racer_call('server-function', name))

    def server_function_(self, name=None) -> RacerResult:
        return self.racer_call('server-function', name)

    def server_value(self, name=None) -> str:
        return str(self.racer_call('server-value', name))

    def server_value_(self, name=None) -> RacerResult:
        return self.racer_call('server-value', name)

    def set_attribute_filler(self, abox=None, individual=None, value=None, attribute=None) -> str:
        return str(self.racer_call('set-attribute-filler', abox, individual, value, attribute, attribute))

    def set_attribute_filler_(self, abox=None, individual=None, value=None, attribute=None) -> RacerResult:
        return self.racer_call('set-attribute-filler', abox, individual, value, attribute, attribute)

    def set_current_abox(self, abox=None) -> str:
        return str(self.racer_call('set-current-abox', abox))

    def set_current_abox_(self, abox=None) -> RacerResult:
        return self.racer_call('set-current-abox', abox)

    def set_current_tbox(self, tbox=None) -> str:
        return str(self.racer_call('set-current-tbox', tbox))

    def set_current_tbox_(self, tbox=None) -> RacerResult:
        return self.racer_call('set-current-tbox', tbox)

    def set_data_box(self, name=None) -> str:
        return str(self.racer_call('set-data-box', name))

    def set_data_box_(self, name=None) -> RacerResult:
        return self.racer_call('set-data-box', name)

    def set_edge_label_for_non_existent_edges(self, *key_args) -> str:
        return str(self.racer_call('set-edge-label-for-non-existent-edges', key_args))

    def set_edge_label_for_non_existent_edges_(self, *key_args) -> RacerResult:
        return self.racer_call('set-edge-label-for-non-existent-edges', key_args)

    def set_find_abox(self, abox_name1=None, abox_name2=None) -> str:
        return str(self.racer_call('set-find-abox', abox_name1, abox_name2))

    def set_find_abox_(self, abox_name1=None, abox_name2=None) -> RacerResult:
        return self.racer_call('set-find-abox', abox_name1, abox_name2)

    def set_find_tbox(self, tbox_name1=None, tbox_name2=None) -> str:
        return str(self.racer_call('set-find-tbox', tbox_name1, tbox_name2))

    def set_find_tbox_(self, tbox_name1=None, tbox_name2=None) -> RacerResult:
        return self.racer_call('set-find-tbox', tbox_name1, tbox_name2)

    def set_initial_size_of_process_pool(self, n=None) -> str:
        return str(self.racer_call('set-initial-size-of-process-pool', n))

    def set_initial_size_of_process_pool_(self, n=None) -> RacerResult:
        return self.racer_call('set-initial-size-of-process-pool', n)

    def set_max_no_of_tuples_bound(self, n=None) -> str:
        return str(self.racer_call('set-max-no-of-tuples-bound', n))

    def set_max_no_of_tuples_bound_(self, n=None) -> RacerResult:
        return self.racer_call('set-max-no-of-tuples-bound', n)

    def set_maximum_size_of_process_pool(self, n=None) -> str:
        return str(self.racer_call('set-maximum-size-of-process-pool', n))

    def set_maximum_size_of_process_pool_(self, n=None) -> RacerResult:
        return self.racer_call('set-maximum-size-of-process-pool', n)

    def set_mirror_data_box(self, name=None) -> str:
        return str(self.racer_call('set-mirror-data-box', name))

    def set_mirror_data_box_(self, name=None) -> RacerResult:
        return self.racer_call('set-mirror-data-box', name)

    def set_new_ind_counter(self, n=None) -> str:
        return str(self.racer_call('set-new-ind-counter', n))

    def set_new_ind_counter_(self, n=None) -> RacerResult:
        return self.racer_call('set-new-ind-counter', n)

    def set_new_ind_prefix(self, prefix=None) -> str:
        return str(self.racer_call('set-new-ind-prefix', prefix))

    def set_new_ind_prefix_(self, prefix=None) -> RacerResult:
        return self.racer_call('set-new-ind-prefix', prefix)

    def set_nrql_mode(self, mode=None) -> str:
        return str(self.racer_call('set-nrql-mode', mode))

    def set_nrql_mode_(self, mode=None) -> RacerResult:
        return self.racer_call('set-nrql-mode', mode)

    def set_proxy_server(self, proxy=None) -> str:
        return str(self.racer_call('set-proxy-server', proxy))

    def set_proxy_server_(self, proxy=None) -> RacerResult:
        return self.racer_call('set-proxy-server', proxy)

    def set_racer_parameter(self, name=None, value=None) -> str:
        return str(self.racer_call('set-racer-parameter', name, value))

    def set_racer_parameter_(self, name=None, value=None) -> RacerResult:
        return self.racer_call('set-racer-parameter', name, value)

    def set_rcc_box(self, name=None, rcc_type=None, type_=None) -> str:
        return str(self.racer_call('set-rcc-box', name, rcc_type, type_))

    def set_rcc_box_(self, name=None, rcc_type=None, type_=None) -> RacerResult:
        return self.racer_call('set-rcc-box', name, rcc_type, type_)

    def set_rewrite_defined_concepts(self, val=None) -> str:
        return str(self.racer_call('set-rewrite-defined-concepts', val))

    def set_rewrite_defined_concepts_(self, val=None) -> RacerResult:
        return self.racer_call('set-rewrite-defined-concepts', val)

    def set_server_timeout(self, timeout=None) -> str:
        return str(self.racer_call('set-server-timeout', timeout))

    def set_server_timeout_(self, timeout=None) -> RacerResult:
        return self.racer_call('set-server-timeout', timeout)

    def set_substrate_type(self, type_=None) -> str:
        return str(self.racer_call('set-substrate-type', type_))

    def set_substrate_type_(self, type_=None) -> RacerResult:
        return self.racer_call('set-substrate-type', type_)

    def set_unique_name_assumption(self, value=None) -> str:
        return str(self.racer_call('set-unique-name-assumption', value))

    def set_unique_name_assumption_(self, value=None) -> RacerResult:
        return self.racer_call('set-unique-name-assumption', value)

    def show_qbox_for_abox(self, abox=None, definitions_p=None) -> str:
        return str(self.racer_call('show-qbox-for-abox', abox, definitions_p))

    def show_qbox_for_abox_(self, abox=None, definitions_p=None) -> RacerResult:
        return self.racer_call('show-qbox-for-abox', abox, definitions_p)

    def sleeping_cheap_queries(self, *key_args) -> str:
        return str(self.racer_call('sleeping-cheap-queries', key_args))

    def sleeping_cheap_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('sleeping-cheap-queries', key_args)

    def sleeping_cheap_rules(self, *key_args) -> str:
        return str(self.racer_call('sleeping-cheap-rules', key_args))

    def sleeping_cheap_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('sleeping-cheap-rules', key_args)

    def sleeping_expensive_queries(self, *key_args) -> str:
        return str(self.racer_call('sleeping-expensive-queries', key_args))

    def sleeping_expensive_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('sleeping-expensive-queries', key_args)

    def sleeping_expensive_rules(self, *key_args) -> str:
        return str(self.racer_call('sleeping-expensive-rules', key_args))

    def sleeping_expensive_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('sleeping-expensive-rules', key_args)

    def sleeping_queries(self, *key_args) -> str:
        return str(self.racer_call('sleeping-queries', key_args))

    def sleeping_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('sleeping-queries', key_args)

    def sleeping_rules(self, *key_args) -> str:
        return str(self.racer_call('sleeping-rules', key_args))

    def sleeping_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('sleeping-rules', key_args)

    def store_abox_image(self, filename=None, abox=None) -> str:
        return str(self.racer_call('store-abox-image', filename, abox))

    def store_abox_image_(self, filename=None, abox=None) -> RacerResult:
        return self.racer_call('store-abox-image', filename, abox)

    def store_aboxes_image(self, filename=None, aboxes=None) -> str:
        return str(self.racer_call('store-aboxes-image', filename, aboxes))

    def store_aboxes_image_(self, filename=None, aboxes=None) -> RacerResult:
        return self.racer_call('store-aboxes-image', filename, aboxes)

    def store_all_substrates(self, filename=None) -> str:
        return str(self.racer_call('store-all-substrates', filename))

    def store_all_substrates_(self, filename=None) -> RacerResult:
        return self.racer_call('store-all-substrates', filename)

    def store_kb_image(self, filename=None, kb=None) -> str:
        return str(self.racer_call('store-kb-image', filename, kb))

    def store_kb_image_(self, filename=None, kb=None) -> RacerResult:
        return self.racer_call('store-kb-image', filename, kb)

    def store_kbs_image(self, filename=None, kbs=None) -> str:
        return str(self.racer_call('store-kbs-image', filename, kbs))

    def store_kbs_image_(self, filename=None, kbs=None) -> RacerResult:
        return self.racer_call('store-kbs-image', filename, kbs)

    def store_server_image(self, filename=None) -> str:
        return str(self.racer_call('store-server-image', filename))

    def store_server_image_(self, filename=None) -> RacerResult:
        return self.racer_call('store-server-image', filename)

    def store_substrate_for_abox(self, filename=None, for_abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('store-substrate-for-abox', filename, for_abox, type_of_substrate))

    def store_substrate_for_abox_(self, filename=None, for_abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('store-substrate-for-abox', filename, for_abox, type_of_substrate)

    def store_tbox_image(self, filename=None, tbox=None) -> str:
        return str(self.racer_call('store-tbox-image', filename, tbox))

    def store_tbox_image_(self, filename=None, tbox=None) -> RacerResult:
        return self.racer_call('store-tbox-image', filename, tbox)

    def store_tboxes_image(self, tboxes=None, filename=None) -> str:
        return str(self.racer_call('store-tboxes-image', tboxes, filename))

    def store_tboxes_image_(self, tboxes=None, filename=None) -> RacerResult:
        return self.racer_call('store-tboxes-image', tboxes, filename)

    def subscribe1(self, subscriber_name=None, query_concept=None, abox=None, ip=None, port=None, simple_protocol_p=None) -> str:
        return str(self.racer_call('subscribe-1', subscriber_name, query_concept, abox, ip, port, simple_protocol_p))

    def subscribe1_(self, subscriber_name=None, query_concept=None, abox=None, ip=None, port=None, simple_protocol_p=None) -> RacerResult:
        return self.racer_call('subscribe-1', subscriber_name, query_concept, abox, ip, port, simple_protocol_p)

    def subscribe_to(self, *key_args) -> str:
        return str(self.racer_call('subscribe-to', key_args))

    def subscribe_to_(self, *key_args) -> RacerResult:
        return self.racer_call('subscribe-to', key_args)

    def swrl_create_abduction_rules_if_possible(self) -> str:
        return str(self.racer_call('swrl-create-abduction-rules-if-possible'))

    def swrl_create_abduction_rules_if_possible_(self) -> RacerResult:
        return self.racer_call('swrl-create-abduction-rules-if-possible')

    def swrl_create_forward_chainging_rules(self) -> str:
        return str(self.racer_call('swrl-create-forward-chainging-rules'))

    def swrl_create_forward_chainging_rules_(self) -> RacerResult:
        return self.racer_call('swrl-create-forward-chainging-rules')

    def swrl_forward_chaining(self, *key_args) -> str:
        return str(self.racer_call('swrl-forward-chaining', key_args))

    def swrl_forward_chaining_(self, *key_args) -> RacerResult:
        return self.racer_call('swrl-forward-chaining', key_args)

    def symmetric_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('symmetric-p', role_term, tbox))

    def taxonomy(self, tbox=None) -> str:
        return str(self.racer_call('taxonomy', tbox))

    def taxonomy_(self, tbox=None) -> RacerResult:
        return self.racer_call('taxonomy', tbox)

    def tbox_classified_p(self, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-classified-p', tbox))

    def tbox_coherent_p(self, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-coherent-p', tbox))

    def tbox_cyclic_p(self, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-cyclic-p', tbox))

    def tbox_prepared_p(self, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-prepared-p', tbox))

    def terminated_queries(self, *key_args) -> str:
        return str(self.racer_call('terminated-queries', key_args))

    def terminated_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('terminated-queries', key_args)

    def terminated_rules(self, *key_args) -> str:
        return str(self.racer_call('terminated-rules', key_args))

    def terminated_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('terminated-rules', key_args)

    def timenet_answer_query(self, *key_args) -> str:
        return str(self.racer_call('timenet-answer-query', key_args))

    def timenet_answer_query_(self, *key_args) -> RacerResult:
        return self.racer_call('timenet-answer-query', key_args)

    def told_value(self, object_=None, abox=None) -> str:
        return str(self.racer_call('told-value', object_, abox))

    def told_value_(self, object_=None, abox=None) -> RacerResult:
        return self.racer_call('told-value', object_, abox)

    def transitive_p(self, role_term=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('transitive-p', role_term, tbox))

    def transmit_file(self, extension=None, n_bytes_=None) -> str:
        return str(self.racer_call('transmit-file', extension, n_bytes_))

    def transmit_file_(self, extension=None, n_bytes_=None) -> RacerResult:
        return self.racer_call('transmit-file', extension, n_bytes_)

    def triple_store_graphs(self, *key_args) -> str:
        return str(self.racer_call('triple-store-graphs', key_args))

    def triple_store_graphs_(self, *key_args) -> RacerResult:
        return self.racer_call('triple-store-graphs', key_args)

    def triple_store_open_p(self, db_name=None) -> bool:
        return self.return_boolean(self.racer_call('triple-store-open-p', db_name))

    def triple_store_read_file(self, *key_args) -> str:
        return str(self.racer_call('triple-store-read-file', key_args))

    def triple_store_read_file_(self, *key_args) -> RacerResult:
        return self.racer_call('triple-store-read-file', key_args)

    def unapplicable_rules(self, *key_args) -> str:
        return str(self.racer_call('unapplicable-rules', key_args))

    def unapplicable_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('unapplicable-rules', key_args)

    def unbind_all(self) -> str:
        return str(self.racer_call('unbind-all'))

    def unbind_all_(self) -> RacerResult:
        return self.racer_call('unbind-all')

    def unbind1(self, name=None) -> str:
        return str(self.racer_call('unbind1', name))

    def unbind1_(self, name=None) -> RacerResult:
        return self.racer_call('unbind1', name)

    def undefine_all(self) -> str:
        return str(self.racer_call('undefine-all'))

    def undefine_all_(self) -> RacerResult:
        return self.racer_call('undefine-all')

    def undefine_query(self, *key_args) -> str:
        return str(self.racer_call('undefine-query', key_args))

    def undefine_query_(self, *key_args) -> RacerResult:
        return self.racer_call('undefine-query', key_args)

    def undefine1(self, name=None) -> str:
        return str(self.racer_call('undefine1', name))

    def undefine1_(self, name=None) -> RacerResult:
        return self.racer_call('undefine1', name)

    def unpublish1(self, individual=None, abox=None) -> str:
        return str(self.racer_call('unpublish-1', individual, abox))

    def unpublish1_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('unpublish-1', individual, abox)

    def unsubscribe1(self, subscriber_name=None, query_concept=None, abox=None) -> str:
        return str(self.racer_call('unsubscribe-1', subscriber_name, query_concept, abox))

    def unsubscribe1_(self, subscriber_name=None, query_concept=None, abox=None) -> RacerResult:
        return self.racer_call('unsubscribe-1', subscriber_name, query_concept, abox)

    def unsubscribe_from(self, *key_args) -> str:
        return str(self.racer_call('unsubscribe-from', key_args))

    def unsubscribe_from_(self, *key_args) -> RacerResult:
        return self.racer_call('unsubscribe-from', key_args)

    def update_racer(self, *key_args) -> str:
        return str(self.racer_call('update-racer', key_args))

    def update_racer_(self, *key_args) -> RacerResult:
        return self.racer_call('update-racer', key_args)

    def use_individual_synonym_equivalence_classes(self) -> str:
        return str(self.racer_call('use-individual-synonym-equivalence-classes'))

    def use_individual_synonym_equivalence_classes_(self) -> RacerResult:
        return self.racer_call('use-individual-synonym-equivalence-classes')

    def use_injective_variables_by_default(self) -> str:
        return str(self.racer_call('use-injective-variables-by-default'))

    def use_injective_variables_by_default_(self) -> RacerResult:
        return self.racer_call('use-injective-variables-by-default')

    def use_triple_store(self, *key_args) -> str:
        return str(self.racer_call('use-triple-store', key_args))

    def use_triple_store_(self, *key_args) -> RacerResult:
        return self.racer_call('use-triple-store', key_args)

    def verify_with_abox_individuals_list(self, individuals_list=None, abox=None) -> str:
        return str(self.racer_call('verify-with-abox-individuals-list', individuals_list, abox))

    def verify_with_abox_individuals_list_(self, individuals_list=None, abox=None) -> RacerResult:
        return self.racer_call('verify-with-abox-individuals-list', individuals_list, abox)

    def verify_with_concept_tree_list(self, tree_list=None, tbox=None, ignore_error=None) -> str:
        return str(self.racer_call('verify-with-concept-tree-list', tree_list, tbox, ignore_error))

    def verify_with_concept_tree_list_(self, tree_list=None, tbox=None, ignore_error=None) -> RacerResult:
        return self.racer_call('verify-with-concept-tree-list', tree_list, tbox, ignore_error)

    def wait_for_queries_to_terminate(self) -> str:
        return str(self.racer_call('wait-for-queries-to-terminate'))

    def wait_for_queries_to_terminate_(self) -> RacerResult:
        return self.racer_call('wait-for-queries-to-terminate')

    def wait_for_rules_to_terminate(self) -> str:
        return str(self.racer_call('wait-for-rules-to-terminate'))

    def wait_for_rules_to_terminate_(self) -> RacerResult:
        return self.racer_call('wait-for-rules-to-terminate')

    def waiting_cheap_queries(self, *key_args) -> str:
        return str(self.racer_call('waiting-cheap-queries', key_args))

    def waiting_cheap_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('waiting-cheap-queries', key_args)

    def waiting_cheap_rules(self, *key_args) -> str:
        return str(self.racer_call('waiting-cheap-rules', key_args))

    def waiting_cheap_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('waiting-cheap-rules', key_args)

    def waiting_expensive_queries(self, *key_args) -> str:
        return str(self.racer_call('waiting-expensive-queries', key_args))

    def waiting_expensive_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('waiting-expensive-queries', key_args)

    def waiting_expensive_rules(self, *key_args) -> str:
        return str(self.racer_call('waiting-expensive-rules', key_args))

    def waiting_expensive_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('waiting-expensive-rules', key_args)

    def waiting_queries(self, *key_args) -> str:
        return str(self.racer_call('waiting-queries', key_args))

    def waiting_queries_(self, *key_args) -> RacerResult:
        return self.racer_call('waiting-queries', key_args)

    def waiting_rules(self, *key_args) -> str:
        return str(self.racer_call('waiting-rules', key_args))

    def waiting_rules_(self, *key_args) -> RacerResult:
        return self.racer_call('waiting-rules', key_args)

    def xml_read_tbox_file(self, filename=None) -> str:
        return str(self.racer_call('xml-read-tbox-file', filename))

    def xml_read_tbox_file_(self, filename=None) -> RacerResult:
        return self.racer_call('xml-read-tbox-file', filename)

    def abox_consistent_m_p(self, abox_name=None) -> bool:
        return self.return_boolean(self.racer_call('abox-consistent?', abox_name))

    def abox_prepared_m_p(self, abox_name=None) -> bool:
        return self.return_boolean(self.racer_call('abox-prepared?', abox_name))

    def abox_realized_m_p(self, abox_name=None) -> bool:
        return self.return_boolean(self.racer_call('abox-realized?', abox_name))

    def abox_una_consistent_m_p(self, abox_name=None) -> bool:
        return self.return_boolean(self.racer_call('abox-una-consistent?', abox_name))

    def add_doc_entry_m(self) -> str:
        return str(self.racer_call('add-doc-entry'))

    def add_doc_entry_m_(self) -> RacerResult:
        return self.racer_call('add-doc-entry')

    def add_doc_image_data_m(self, url=None, type_=None, bytes_=None) -> str:
        return str(self.racer_call('add-doc-image-data', url, type_, bytes_))

    def add_doc_image_data_m_(self, url=None, type_=None, bytes_=None) -> RacerResult:
        return self.racer_call('add-doc-image-data', url, type_, bytes_)

    def add_doc_image_data_from_file_m(self, url=None, type_=None, pathname=None) -> str:
        return str(self.racer_call('add-doc-image-data-from-file', url, type_, pathname))

    def add_doc_image_data_from_file_m_(self, url=None, type_=None, pathname=None) -> RacerResult:
        return self.racer_call('add-doc-image-data-from-file', url, type_, pathname)

    def add_doc_image_file_m(self, url=None, type_=None, pathname=None) -> str:
        return str(self.racer_call('add-doc-image-file', url, type_, pathname))

    def add_doc_image_file_m_(self, url=None, type_=None, pathname=None) -> RacerResult:
        return self.racer_call('add-doc-image-file', url, type_, pathname)

    def add_doc_phrase_m(self, label=None, string=None) -> str:
        return str(self.racer_call('add-doc-phrase', label, string))

    def add_doc_phrase_m_(self, label=None, string=None) -> RacerResult:
        return self.racer_call('add-doc-phrase', label, string)

    def all_different_m(self, *key_args) -> str:
        return str(self.racer_call('all-different', key_args))

    def all_different_m_(self, *key_args) -> RacerResult:
        return self.racer_call('all-different', key_args)

    def apply_abox_rule_m(self, *key_args) -> str:
        return str(self.racer_call('apply-abox-rule', key_args))

    def apply_abox_rule_m_(self, *key_args) -> RacerResult:
        return self.racer_call('apply-abox-rule', key_args)

    def apply_abox_rule_under_premise_m(self, *key_args) -> str:
        return str(self.racer_call('apply-abox-rule-under-premise', key_args))

    def apply_abox_rule_under_premise_m_(self, *key_args) -> RacerResult:
        return self.racer_call('apply-abox-rule-under-premise', key_args)

    def apply_abox_rule_under_premise1_m(self, *key_args) -> str:
        return str(self.racer_call('apply-abox-rule-under-premise1', key_args))

    def apply_abox_rule_under_premise1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('apply-abox-rule-under-premise1', key_args)

    def apply_abox_rule1_m(self, *key_args) -> str:
        return str(self.racer_call('apply-abox-rule1', key_args))

    def apply_abox_rule1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('apply-abox-rule1', key_args)

    def asymmetric_m(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('asymmetric', rolename, tbox))

    def asymmetric_m_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('asymmetric', rolename, tbox)

    def asymmetric_m_p(self, role_term=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('asymmetric?', role_term, tbox_name))

    def attribute_domain_m(self, attribute_name=None, tbox=None) -> str:
        return str(self.racer_call('attribute-domain', attribute_name, tbox))

    def attribute_domain_m_(self, attribute_name=None, tbox=None) -> RacerResult:
        return self.racer_call('attribute-domain', attribute_name, tbox)

    def attribute_filler_m(self, individual=None, value=None, attribute=None, type_=None) -> str:
        return str(self.racer_call('attribute-filler', individual, value, attribute, type_))

    def attribute_filler_m_(self, individual=None, value=None, attribute=None, type_=None) -> RacerResult:
        return self.racer_call('attribute-filler', individual, value, attribute, type_)

    def cd_attribute_m_p(self, attribute=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('cd-attribute?', attribute, tbox_name))

    def cd_object_m_p(self, object_name=None, abox_name=None) -> bool:
        return self.return_boolean(self.racer_call('cd-object?', object_name, abox_name))

    def clone_abox_m(self, *key_args) -> str:
        return str(self.racer_call('clone-abox', key_args))

    def clone_abox_m_(self, *key_args) -> RacerResult:
        return self.racer_call('clone-abox', key_args)

    def clone_tbox_m(self, *key_args) -> str:
        return str(self.racer_call('clone-tbox', key_args))

    def clone_tbox_m_(self, *key_args) -> RacerResult:
        return self.racer_call('clone-tbox', key_args)

    def compute_abox_difference_m(self, *key_args) -> str:
        return str(self.racer_call('compute-abox-difference', key_args))

    def compute_abox_difference_m_(self, *key_args) -> RacerResult:
        return self.racer_call('compute-abox-difference', key_args)

    def compute_abox_difference_alternative_m(self, *key_args) -> str:
        return str(self.racer_call('compute-abox-difference-alternative', key_args))

    def compute_abox_difference_alternative_m_(self, *key_args) -> RacerResult:
        return self.racer_call('compute-abox-difference-alternative', key_args)

    def concept_ancestors_m(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('concept-ancestors', concept_term, tbox))

    def concept_ancestors_m_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('concept-ancestors', concept_term, tbox)

    def concept_children_m(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('concept-children', concept_term, tbox))

    def concept_children_m_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('concept-children', concept_term, tbox)

    def concept_descendants_m(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('concept-descendants', concept_term, tbox))

    def concept_descendants_m_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('concept-descendants', concept_term, tbox)

    def concept_disjoint_m_p(self, concept1=None, concept2=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('concept-disjoint?', concept1, concept2, tbox_name))

    def concept_equivalent_m_p(self, concept1=None, concept2=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('concept-equivalent?', concept1, concept2, tbox_name))

    def concept_instances_m(self, concept_term=None, abox=None, candidates=None) -> str:
        return str(self.racer_call('concept-instances', concept_term, abox, candidates))

    def concept_instances_m_(self, concept_term=None, abox=None, candidates=None) -> RacerResult:
        return self.racer_call('concept-instances', concept_term, abox, candidates)

    def concept_is_primitive_m_p(self, concept_name=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('concept-is-primitive?', concept_name, tbox))

    def concept_parents_m(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('concept-parents', concept_term, tbox))

    def concept_parents_m_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('concept-parents', concept_term, tbox)

    def concept_satisfiable_m_p(self, concept1=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('concept-satisfiable?', concept1, tbox_name))

    def concept_subsumes_m_p(self, concept1=None, concept2=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('concept-subsumes?', concept1, concept2, tbox_name))

    def concept_synonyms_m(self, concept_term=None, tbox=None) -> str:
        return str(self.racer_call('concept-synonyms', concept_term, tbox))

    def concept_synonyms_m_(self, concept_term=None, tbox=None) -> RacerResult:
        return self.racer_call('concept-synonyms', concept_term, tbox)

    def concept_m_p(self, concept_name=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('concept?', concept_name, tbox_name))

    def constrained_m(self, individual=None, object_=None, attribute=None) -> str:
        return str(self.racer_call('constrained', individual, object_, attribute))

    def constrained_m_(self, individual=None, object_=None, attribute=None) -> RacerResult:
        return self.racer_call('constrained', individual, object_, attribute)

    def constraint_entailed_m_p(self, constraint=None, abox_name=None) -> bool:
        return self.return_boolean(self.racer_call('constraint-entailed?', constraint, abox_name))

    def constraints_m(self, *key_args) -> str:
        return str(self.racer_call('constraints', key_args))

    def constraints_m_(self, *key_args) -> RacerResult:
        return self.racer_call('constraints', key_args)

    def data_edge_m(self, from_=None, to=None, data_relation=None, racer_descr=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('data-edge', from_, to, data_relation, racer_descr, abox, type_of_substrate))

    def data_edge_m_(self, from_=None, to=None, data_relation=None, racer_descr=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('data-edge', from_, to, data_relation, racer_descr, abox, type_of_substrate)

    def data_node_m(self, name=None, descr=None, racer_descr=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('data-node', name, descr, racer_descr, abox, type_of_substrate))

    def data_node_m_(self, name=None, descr=None, racer_descr=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('data-node', name, descr, racer_descr, abox, type_of_substrate)

    def datatype_role_filler_m(self, individual=None, value=None, role=None, type_=None) -> str:
        return str(self.racer_call('datatype-role-filler', individual, value, role, type_))

    def datatype_role_filler_m_(self, individual=None, value=None, role=None, type_=None) -> RacerResult:
        return self.racer_call('datatype-role-filler', individual, value, role, type_)

    def def_and_exec_query_m(self, *key_args) -> str:
        return str(self.racer_call('def-and-exec-query', key_args))

    def def_and_exec_query_m_(self, *key_args) -> RacerResult:
        return self.racer_call('def-and-exec-query', key_args)

    def def_and_prep_query_m(self, *key_args) -> str:
        return str(self.racer_call('def-and-prep-query', key_args))

    def def_and_prep_query_m_(self, *key_args) -> RacerResult:
        return self.racer_call('def-and-prep-query', key_args)

    def defcon_m(self, name=None, value=None) -> str:
        return str(self.racer_call('defcon', name, value))

    def defcon_m_(self, name=None, value=None) -> RacerResult:
        return self.racer_call('defcon', name, value)

    def define_m(self, name=None, arglist=None) -> str:
        return str(self.racer_call('define', name, arglist))

    def define_m_(self, name=None, arglist=None) -> RacerResult:
        return self.racer_call('define', name, arglist)

    def define_abox_m(self, *key_args) -> str:
        return str(self.racer_call('define-abox', key_args))

    def define_abox_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-abox', key_args)

    def define_concept_m(self, name=None, definition=None) -> str:
        return str(self.racer_call('define-concept', name, definition))

    def define_concept_m_(self, name=None, definition=None) -> RacerResult:
        return self.racer_call('define-concept', name, definition)

    def define_concrete_domain_attribute_m(self, *key_args) -> str:
        return str(self.racer_call('define-concrete-domain-attribute', key_args))

    def define_concrete_domain_attribute_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-concrete-domain-attribute', key_args)

    def define_datatype_property_m(self, *key_args) -> str:
        return str(self.racer_call('define-datatype-property', key_args))

    def define_datatype_property_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-datatype-property', key_args)

    def define_disjoint_primitive_concept_m(self, name=None, disjoint_list=None, definition=None) -> str:
        return str(self.racer_call('define-disjoint-primitive-concept', name, disjoint_list, definition))

    def define_disjoint_primitive_concept_m_(self, name=None, disjoint_list=None,
                                             definition=None) -> RacerResult:
        return self.racer_call('define-disjoint-primitive-concept', name, disjoint_list, definition)

    def define_distinct_individual_m(self, individual_name=None, concept=None) -> str:
        return str(self.racer_call('define-distinct-individual', individual_name, concept))

    def define_distinct_individual_m_(self, individual_name=None, concept=None) -> RacerResult:
        return self.racer_call('define-distinct-individual', individual_name, concept)

    def define_event_assertion_m(self, assertion=None) -> str:
        return str(self.racer_call('define-event-assertion', assertion))

    def define_event_assertion_m_(self, assertion=None) -> RacerResult:
        return self.racer_call('define-event-assertion', assertion)

    def define_event_rule_m(self, *key_args) -> str:
        return str(self.racer_call('define-event-rule', key_args))

    def define_event_rule_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-event-rule', key_args)

    def define_individual_m(self, individual_name=None, concept=None) -> str:
        return str(self.racer_call('define-individual', individual_name, concept))

    def define_individual_m_(self, individual_name=None, concept=None) -> RacerResult:
        return self.racer_call('define-individual', individual_name, concept)

    def define_prefix_m(self, prefix=None, mapping=None) -> str:
        return str(self.racer_call('define-prefix', prefix, mapping))

    def define_prefix_m_(self, prefix=None, mapping=None) -> RacerResult:
        return self.racer_call('define-prefix', prefix, mapping)

    def define_primitive_attribute_m(self, *key_args) -> str:
        return str(self.racer_call('define-primitive-attribute', key_args))

    def define_primitive_attribute_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-primitive-attribute', key_args)

    def define_primitive_concept_m(self, name=None, definition=None) -> str:
        return str(self.racer_call('define-primitive-concept', name, definition))

    def define_primitive_concept_m_(self, name=None, definition=None) -> RacerResult:
        return self.racer_call('define-primitive-concept', name, definition)

    def define_primitive_role_m(self, *key_args) -> str:
        return str(self.racer_call('define-primitive-role', key_args))

    def define_primitive_role_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-primitive-role', key_args)

    def define_rule_m(self, *key_args) -> str:
        return str(self.racer_call('define-rule', key_args))

    def define_rule_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-rule', key_args)

    def define_tbox_m(self, *key_args) -> str:
        return str(self.racer_call('define-tbox', key_args))

    def define_tbox_m_(self, *key_args) -> RacerResult:
        return self.racer_call('define-tbox', key_args)

    def defpar_m(self, name=None, value=None) -> str:
        return str(self.racer_call('defpar', name, value))

    def defpar_m_(self, name=None, value=None) -> RacerResult:
        return self.racer_call('defpar', name, value)

    def defquery_m(self, *key_args) -> str:
        return str(self.racer_call('defquery', key_args))

    def defquery_m_(self, *key_args) -> RacerResult:
        return self.racer_call('defquery', key_args)

    def del_data_edge_m(self, from_=None, to=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('del-data-edge', from_, to, abox, type_of_substrate))

    def del_data_edge_m_(self, from_=None, to=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('del-data-edge', from_, to, abox, type_of_substrate)

    def del_data_node_m(self, name=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('del-data-node', name, abox, type_of_substrate))

    def del_data_node_m_(self, name=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('del-data-node', name, abox, type_of_substrate)

    def del_doc_entry_m(self, label=None) -> str:
        return str(self.racer_call('del-doc-entry', label))

    def del_doc_entry_m_(self, label=None) -> RacerResult:
        return self.racer_call('del-doc-entry', label)

    def del_rcc_edge_m(self) -> str:
        return str(self.racer_call('del-rcc-edge'))

    def del_rcc_edge_m_(self) -> RacerResult:
        return self.racer_call('del-rcc-edge')

    def del_rcc_node_m(self) -> str:
        return str(self.racer_call('del-rcc-node'))

    def del_rcc_node_m_(self) -> RacerResult:
        return self.racer_call('del-rcc-node')

    def delete_abox_m(self, abox=None) -> str:
        return str(self.racer_call('delete-abox', abox))

    def delete_abox_m_(self, abox=None) -> RacerResult:
        return self.racer_call('delete-abox', abox)

    def delete_tbox_m(self, tbox=None) -> str:
        return str(self.racer_call('delete-tbox', tbox))

    def delete_tbox_m_(self, tbox=None) -> RacerResult:
        return self.racer_call('delete-tbox', tbox)

    def description_implies_m_p(self, a=None, b=None) -> bool:
        return self.return_boolean(self.racer_call('description-implies?', a, b))

    def different_from_m(self, individual_name1=None, individual_name2=None) -> str:
        return str(self.racer_call('different-from', individual_name1, individual_name2))

    def different_from_m_(self, individual_name1=None, individual_name2=None) -> RacerResult:
        return self.racer_call('different-from', individual_name1, individual_name2)

    def direct_predecessors_m(self, role_term=None, ind_filler=None, abox=None) -> str:
        return str(self.racer_call('direct-predecessors', role_term, ind_filler, abox))

    def direct_predecessors_m_(self, role_term=None, ind_filler=None, abox=None) -> RacerResult:
        return self.racer_call('direct-predecessors', role_term, ind_filler, abox)

    def disjoint_m(self, *key_args) -> str:
        return str(self.racer_call('disjoint', key_args))

    def disjoint_m_(self, *key_args) -> RacerResult:
        return self.racer_call('disjoint', key_args)

    def domain_m(self, rolename=None, concept=None, tbox=None, errorp=None) -> str:
        return str(self.racer_call('domain', rolename, concept, tbox, errorp))

    def domain_m_(self, rolename=None, concept=None, tbox=None, errorp=None) -> RacerResult:
        return self.racer_call('domain', rolename, concept, tbox, errorp)

    def edge_description_m(self, from_=None, to=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('edge-description', from_, to, abox, type_of_substrate))

    def edge_description_m_(self, from_=None, to=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('edge-description', from_, to, abox, type_of_substrate)

    def edge_label_m(self, from_=None, to=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('edge-label', from_, to, abox, type_of_substrate))

    def edge_label_m_(self, from_=None, to=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('edge-label', from_, to, abox, type_of_substrate)

    def equivalent_m(self, left=None, right=None) -> str:
        return str(self.racer_call('equivalent', left, right))

    def equivalent_m_(self, left=None, right=None) -> RacerResult:
        return self.racer_call('equivalent', left, right)

    def feature_m_p(self, role_term=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('feature?', role_term, tbox_name))

    def firerule_m(self, *key_args) -> str:
        return str(self.racer_call('firerule', key_args))

    def firerule_m_(self, *key_args) -> RacerResult:
        return self.racer_call('firerule', key_args)

    def firerule_under_premise_m(self, *key_args) -> str:
        return str(self.racer_call('firerule-under-premise', key_args))

    def firerule_under_premise_m_(self, *key_args) -> RacerResult:
        return self.racer_call('firerule-under-premise', key_args)

    def firerule_under_premise1_m(self, *key_args) -> str:
        return str(self.racer_call('firerule-under-premise1', key_args))

    def firerule_under_premise1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('firerule-under-premise1', key_args)

    def firerule1_m(self, *key_args) -> str:
        return str(self.racer_call('firerule1', key_args))

    def firerule1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('firerule1', key_args)

    def forget_m(self, *key_args) -> str:
        return str(self.racer_call('forget', key_args))

    def forget_m_(self, *key_args) -> RacerResult:
        return self.racer_call('forget', key_args)

    def functional_m(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('functional', rolename, tbox))

    def functional_m_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('functional', rolename, tbox)

    def get_concept_definition_m(self, concept_name=None, tbox=None) -> str:
        return str(self.racer_call('get-concept-definition', concept_name, tbox))

    def get_concept_definition_m_(self, concept_name=None, tbox=None) -> RacerResult:
        return self.racer_call('get-concept-definition', concept_name, tbox)

    def get_concept_negated_definition_m(self, concept_name=None, tbox=None) -> str:
        return str(self.racer_call('get-concept-negated-definition', concept_name, tbox))

    def get_concept_negated_definition_m_(self, concept_name=None, tbox=None) -> RacerResult:
        return self.racer_call('get-concept-negated-definition', concept_name, tbox)

    def implies_m(self, left=None, right=None) -> str:
        return str(self.racer_call('implies', left, right))

    def implies_m_(self, left=None, right=None) -> RacerResult:
        return self.racer_call('implies', left, right)

    def implies_role_m(self, rolename1=None, rolename2=None, tbox=None) -> str:
        return str(self.racer_call('implies-role', rolename1, rolename2, tbox))

    def implies_role_m_(self, rolename1=None, rolename2=None, tbox=None) -> RacerResult:
        return self.racer_call('implies-role', rolename1, rolename2, tbox)

    def in_abox_m(self, abox_name=None, tbox_name=None) -> str:
        return str(self.racer_call('in-abox', abox_name, tbox_name))

    def in_abox_m_(self, abox_name=None, tbox_name=None) -> RacerResult:
        return self.racer_call('in-abox', abox_name, tbox_name)

    def in_data_box_m(self, name=None) -> str:
        return str(self.racer_call('in-data-box', name))

    def in_data_box_m_(self, name=None) -> RacerResult:
        return self.racer_call('in-data-box', name)

    def in_knowledge_base_m(self, *key_args) -> str:
        return str(self.racer_call('in-knowledge-base', key_args))

    def in_knowledge_base_m_(self, *key_args) -> RacerResult:
        return self.racer_call('in-knowledge-base', key_args)

    def in_mirror_data_box_m(self, name=None) -> str:
        return str(self.racer_call('in-mirror-data-box', name))

    def in_mirror_data_box_m_(self, name=None) -> RacerResult:
        return self.racer_call('in-mirror-data-box', name)

    def in_rcc_box_m(self, name=None, rcc_type=None, type_=None) -> str:
        return str(self.racer_call('in-rcc-box', name, rcc_type, type_))

    def in_rcc_box_m_(self, name=None, rcc_type=None, type_=None) -> RacerResult:
        return self.racer_call('in-rcc-box', name, rcc_type, type_)

    def in_tbox_m(self, *key_args) -> str:
        return str(self.racer_call('in-tbox', key_args))

    def in_tbox_m_(self, *key_args) -> RacerResult:
        return self.racer_call('in-tbox', key_args)

    def individual_antonyms_m(self, individual=None, told_only=None, abox_name=None) -> str:
        return str(self.racer_call('individual-antonyms', individual, told_only, abox_name))

    def individual_antonyms_m_(self, individual=None, told_only=None, abox_name=None) -> RacerResult:
        return self.racer_call('individual-antonyms', individual, told_only, abox_name)

    def individual_attribute_fillers_m(self, ind=None, attribute=None, abox=None) -> str:
        return str(self.racer_call('individual-attribute-fillers', ind, attribute, abox))

    def individual_attribute_fillers_m_(self, ind=None, attribute=None, abox=None) -> RacerResult:
        return self.racer_call('individual-attribute-fillers', ind, attribute, abox)

    def individual_direct_types_m(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('individual-direct-types', individual_name, abox))

    def individual_direct_types_m_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('individual-direct-types', individual_name, abox)

    def individual_filled_roles_m(self, ind_predecessor=None, ind_filler=None, abox=None) -> str:
        return str(self.racer_call('individual-filled-roles', ind_predecessor, ind_filler, abox))

    def individual_filled_roles_m_(self, ind_predecessor=None, ind_filler=None, abox=None) -> RacerResult:
        return self.racer_call('individual-filled-roles', ind_predecessor, ind_filler, abox)

    def individual_fillers_m(self, ind_predecessor=None, role_term=None, abox=None) -> str:
        return str(self.racer_call('individual-fillers', ind_predecessor, role_term, abox))

    def individual_fillers_m_(self, ind_predecessor=None, role_term=None, abox=None) -> RacerResult:
        return self.racer_call('individual-fillers', ind_predecessor, role_term, abox)

    def individual_instance_m_p(self, individual=None, concept=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('individual-instance?', individual, concept, abox))

    def individual_synonyms_m(self, individual=None, told_only=None, abox_name=None) -> str:
        return str(self.racer_call('individual-synonyms', individual, told_only, abox_name))

    def individual_synonyms_m_(self, individual=None, told_only=None, abox_name=None) -> RacerResult:
        return self.racer_call('individual-synonyms', individual, told_only, abox_name)

    def individual_told_attribute_value_m(self, ind=None, attribute=None, abox=None) -> str:
        return str(self.racer_call('individual-told-attribute-value', ind, attribute, abox))

    def individual_told_attribute_value_m_(self, ind=None, attribute=None, abox=None) -> RacerResult:
        return self.racer_call('individual-told-attribute-value', ind, attribute, abox)

    def individual_told_datatype_fillers_m(self, ind=None, datatype_role=None, abox=None) -> str:
        return str(self.racer_call('individual-told-datatype-fillers', ind, datatype_role, abox))

    def individual_told_datatype_fillers_m_(self, ind=None, datatype_role=None, abox=None) -> RacerResult:
        return self.racer_call('individual-told-datatype-fillers', ind, datatype_role, abox)

    def individual_types_m(self, individual_name=None, abox=None) -> str:
        return str(self.racer_call('individual-types', individual_name, abox))

    def individual_types_m_(self, individual_name=None, abox=None) -> RacerResult:
        return self.racer_call('individual-types', individual_name, abox)

    def individual_m_p(self, individual_name=None, abox_name=None) -> bool:
        return self.return_boolean(self.racer_call('individual?', individual_name, abox_name))

    def individuals_equal_m_p(self, individual1=None, individual2=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('individuals-equal?', individual1, individual2, abox))

    def individuals_not_equal_m_p(self, individual1=None, individual2=None, abox=None) -> bool:
        return self.return_boolean(self.racer_call('individuals-not-equal?', individual1, individual2, abox))

    def individuals_related_m_p(self, individual1=None, individual2=None, role_term=None) -> bool:
        return self.return_boolean(self.racer_call('individuals-related?', individual1, individual2, role_term))

    def init_publications_m(self, abox=None) -> str:
        return str(self.racer_call('init-publications', abox))

    def init_publications_m_(self, abox=None) -> RacerResult:
        return self.racer_call('init-publications', abox)

    def init_subscriptions_m(self, abox=None) -> str:
        return str(self.racer_call('init-subscriptions', abox))

    def init_subscriptions_m_(self, abox=None) -> RacerResult:
        return self.racer_call('init-subscriptions', abox)

    def instance_m(self, name=None, concept=None) -> str:
        return str(self.racer_call('instance', name, concept))

    def instance_m_(self, name=None, concept=None) -> RacerResult:
        return self.racer_call('instance', name, concept)

    def inverse_m(self, rolename=None, inverse_role=None, tbox=None) -> str:
        return str(self.racer_call('inverse', rolename, inverse_role, tbox))

    def inverse_m_(self, rolename=None, inverse_role=None, tbox=None) -> RacerResult:
        return self.racer_call('inverse', rolename, inverse_role, tbox)

    def irreflexive_m(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('irreflexive', rolename, tbox))

    def irreflexive_m_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('irreflexive', rolename, tbox)

    def irreflexive_m_p(self, role_term=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('irreflexive?', role_term, tbox_name))

    def node_description_m(self, name=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('node-description', name, abox, type_of_substrate))

    def node_description_m_(self, name=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('node-description', name, abox, type_of_substrate)

    def node_label_m(self, name=None, abox=None, type_of_substrate=None) -> str:
        return str(self.racer_call('node-label', name, abox, type_of_substrate))

    def node_label_m_(self, name=None, abox=None, type_of_substrate=None) -> RacerResult:
        return self.racer_call('node-label', name, abox, type_of_substrate)

    def prepare_abox_query_m(self, *key_args) -> str:
        return str(self.racer_call('prepare-abox-query', key_args))

    def prepare_abox_query_m_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-abox-query', key_args)

    def prepare_abox_query1_m(self, *key_args) -> str:
        return str(self.racer_call('prepare-abox-query1', key_args))

    def prepare_abox_query1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-abox-query1', key_args)

    def prepare_abox_rule_m(self, *key_args) -> str:
        return str(self.racer_call('prepare-abox-rule', key_args))

    def prepare_abox_rule_m_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-abox-rule', key_args)

    def prepare_abox_rule1_m(self, *key_args) -> str:
        return str(self.racer_call('prepare-abox-rule1', key_args))

    def prepare_abox_rule1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-abox-rule1', key_args)

    def prepare_tbox_query_m(self, *key_args) -> str:
        return str(self.racer_call('prepare-tbox-query', key_args))

    def prepare_tbox_query_m_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-tbox-query', key_args)

    def prepare_tbox_query1_m(self, *key_args) -> str:
        return str(self.racer_call('prepare-tbox-query1', key_args))

    def prepare_tbox_query1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('prepare-tbox-query1', key_args)

    def preprule_m(self, *key_args) -> str:
        return str(self.racer_call('preprule', key_args))

    def preprule_m_(self, *key_args) -> RacerResult:
        return self.racer_call('preprule', key_args)

    def preprule1_m(self, *key_args) -> str:
        return str(self.racer_call('preprule1', key_args))

    def preprule1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('preprule1', key_args)

    def pretrieve_m(self, *key_args) -> str:
        return str(self.racer_call('pretrieve', key_args))

    def pretrieve_m_(self, *key_args) -> RacerResult:
        return self.racer_call('pretrieve', key_args)

    def publish_m(self, individual=None, abox=None) -> str:
        return str(self.racer_call('publish', individual, abox))

    def publish_m_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('publish', individual, abox)

    def range_m(self, rolename=None, concept=None, tbox=None, errorp=None) -> str:
        return str(self.racer_call('range', rolename, concept, tbox, errorp))

    def range_m_(self, rolename=None, concept=None, tbox=None, errorp=None) -> RacerResult:
        return self.racer_call('range', rolename, concept, tbox, errorp)

    def rcc_consistent_m_p(self, abox=None, type_of_substrate=None) -> bool:
        return self.return_boolean(self.racer_call('rcc-consistent?', abox, type_of_substrate))

    def rcc_edge_m(self) -> str:
        return str(self.racer_call('rcc-edge'))

    def rcc_edge_m_(self) -> RacerResult:
        return self.racer_call('rcc-edge')

    def rcc_edge_description_m(self) -> str:
        return str(self.racer_call('rcc-edge-description'))

    def rcc_edge_description_m_(self) -> RacerResult:
        return self.racer_call('rcc-edge-description')

    def rcc_edge_label_m(self) -> str:
        return str(self.racer_call('rcc-edge-label'))

    def rcc_edge_label_m_(self) -> RacerResult:
        return self.racer_call('rcc-edge-label')

    def rcc_instance_m(self) -> str:
        return str(self.racer_call('rcc-instance'))

    def rcc_instance_m_(self) -> RacerResult:
        return self.racer_call('rcc-instance')

    def rcc_node_m(self) -> str:
        return str(self.racer_call('rcc-node'))

    def rcc_node_m_(self) -> RacerResult:
        return self.racer_call('rcc-node')

    def rcc_node_description_m(self) -> str:
        return str(self.racer_call('rcc-node-description'))

    def rcc_node_description_m_(self) -> RacerResult:
        return self.racer_call('rcc-node-description')

    def rcc_node_label_m(self) -> str:
        return str(self.racer_call('rcc-node-label'))

    def rcc_node_label_m_(self) -> RacerResult:
        return self.racer_call('rcc-node-label')

    def rcc_related_m(self) -> str:
        return str(self.racer_call('rcc-related'))

    def rcc_related_m_(self) -> RacerResult:
        return self.racer_call('rcc-related')

    def rcc_synonym_m(self, role=None, rcc_relation=None) -> str:
        return str(self.racer_call('rcc-synonym', role, rcc_relation))

    def rcc_synonym_m_(self, role=None, rcc_relation=None) -> RacerResult:
        return self.racer_call('rcc-synonym', role, rcc_relation)

    def reflexive_m(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('reflexive', rolename, tbox))

    def reflexive_m_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('reflexive', rolename, tbox)

    def reflexive_m_p(self, role_term=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('reflexive?', role_term, tbox_name))

    def related_m(self, left_name=None, right_name=None, role_name=None) -> str:
        return str(self.racer_call('related', left_name, right_name, role_name))

    def related_m_(self, left_name=None, right_name=None, role_name=None) -> RacerResult:
        return self.racer_call('related', left_name, right_name, role_name)

    def related_individuals_m(self, role_term=None, abox_name=None) -> str:
        return str(self.racer_call('related-individuals', role_term, abox_name))

    def related_individuals_m_(self, role_term=None, abox_name=None) -> RacerResult:
        return self.racer_call('related-individuals', role_term, abox_name)

    def retrieve_m(self, *key_args) -> str:
        return str(self.racer_call('retrieve', key_args))

    def retrieve_m_(self, *key_args) -> RacerResult:
        return self.racer_call('retrieve', key_args)

    def retrieve_under_premise_m(self, *key_args) -> str:
        return str(self.racer_call('retrieve-under-premise', key_args))

    def retrieve_under_premise_m_(self, *key_args) -> RacerResult:
        return self.racer_call('retrieve-under-premise', key_args)

    def retrieve_under_premise1_m(self, *key_args) -> str:
        return str(self.racer_call('retrieve-under-premise1', key_args))

    def retrieve_under_premise1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('retrieve-under-premise1', key_args)

    def retrieve_with_explanation_m(self, *key_args) -> str:
        return str(self.racer_call('retrieve-with-explanation', key_args))

    def retrieve_with_explanation_m_(self, *key_args) -> RacerResult:
        return self.racer_call('retrieve-with-explanation', key_args)

    def retrieve1_m(self, *key_args) -> str:
        return str(self.racer_call('retrieve1', key_args))

    def retrieve1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('retrieve1', key_args)

    def role_ancestors_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-ancestors', role_term, tbox))

    def role_ancestors_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-ancestors', role_term, tbox)

    def role_children_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-children', role_term, tbox))

    def role_children_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-children', role_term, tbox)

    def role_descendants_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-descendants', role_term, tbox))

    def role_descendants_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-descendants', role_term, tbox)

    def role_disjoint_m_p(self, role_term1=None, role_term2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-disjoint?', role_term1, role_term2, tbox))

    def role_domain_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-domain', role_term, tbox))

    def role_domain_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-domain', role_term, tbox)

    def role_equivalent_m_p(self, role_term1=None, role_term2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-equivalent?', role_term1, role_term2, tbox))

    def role_inverse_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-inverse', role_term, tbox))

    def role_inverse_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-inverse', role_term, tbox)

    def role_parents_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-parents', role_term, tbox))

    def role_parents_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-parents', role_term, tbox)

    def role_range_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-range', role_term, tbox))

    def role_range_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-range', role_term, tbox)

    def role_satisfiable_m_p(self, role=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-satisfiable?', role, tbox))

    def role_subsumes_m_p(self, role_term1=None, role_term2=None, tbox=None) -> bool:
        return self.return_boolean(self.racer_call('role-subsumes?', role_term1, role_term2, tbox))

    def role_synonyms_m(self, role_term=None, tbox=None) -> str:
        return str(self.racer_call('role-synonyms', role_term, tbox))

    def role_synonyms_m_(self, role_term=None, tbox=None) -> RacerResult:
        return self.racer_call('role-synonyms', role_term, tbox)

    def role_m_p(self, role_term=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('role?', role_term, tbox_name))

    def roles_disjoint_m(self, role1=None, role2=None, tbox=None) -> str:
        return str(self.racer_call('roles-disjoint', role1, role2, tbox))

    def roles_disjoint_m_(self, role1=None, role2=None, tbox=None) -> RacerResult:
        return self.racer_call('roles-disjoint', role1, role2, tbox)

    def roles_equivalent_m(self, role1=None, role2=None, tbox=None) -> str:
        return str(self.racer_call('roles-equivalent', role1, role2, tbox))

    def roles_equivalent_m_(self, role1=None, role2=None, tbox=None) -> RacerResult:
        return self.racer_call('roles-equivalent', role1, role2, tbox)

    def same_as_m(self, individual_name1=None, individual_name2=None) -> str:
        return str(self.racer_call('same-as', individual_name1, individual_name2))

    def same_as_m_(self, individual_name1=None, individual_name2=None) -> RacerResult:
        return self.racer_call('same-as', individual_name1, individual_name2)

    def same_individual_as_m(self, individual_name1=None, individual_name2=None) -> str:
        return str(self.racer_call('same-individual-as', individual_name1, individual_name2))

    def same_individual_as_m_(self, individual_name1=None, individual_name2=None) -> RacerResult:
        return self.racer_call('same-individual-as', individual_name1, individual_name2)

    def signature_m(self, *key_args) -> str:
        return str(self.racer_call('signature', key_args))

    def signature_m_(self, *key_args) -> RacerResult:
        return self.racer_call('signature', key_args)

    def sparql_answer_query_m(self, *key_args) -> str:
        return str(self.racer_call('sparql-answer-query', key_args))

    def sparql_answer_query_m_(self, *key_args) -> RacerResult:
        return self.racer_call('sparql-answer-query', key_args)

    def sparql_retrieve_m(self, *key_args) -> str:
        return str(self.racer_call('sparql-retrieve', key_args))

    def sparql_retrieve_m_(self, *key_args) -> RacerResult:
        return self.racer_call('sparql-retrieve', key_args)

    def state_m(self, *key_args) -> str:
        return str(self.racer_call('state', key_args))

    def state_m_(self, *key_args) -> RacerResult:
        return self.racer_call('state', key_args)

    def subscribe_m(self, subscriber=None, query_concept=None, abox=None, ip=None, port=None) -> str:
        return str(self.racer_call('subscribe', subscriber, query_concept, abox, ip, port, port))

    def subscribe_m_(self, subscriber=None, query_concept=None, abox=None, ip=None, port=None) -> RacerResult:
        return self.racer_call('subscribe', subscriber, query_concept, abox, ip, port, ip)

    def symmetric_m(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('symmetric', rolename, tbox))

    def symmetric_m_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('symmetric', rolename, tbox)

    def symmetric_m_p(self, role_term=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('symmetric?', role_term, tbox_name))

    def tbox_classified_m_p(self, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-classified?', tbox_name))

    def tbox_coherent_m_p(self, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-coherent?', tbox_name))

    def tbox_cyclic_m_p(self, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-cyclic?', tbox_name))

    def tbox_prepared_m_p(self, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('tbox-prepared?', tbox_name))

    def tbox_retrieve_m(self, *key_args) -> str:
        return str(self.racer_call('tbox-retrieve', key_args))

    def tbox_retrieve_m_(self, *key_args) -> RacerResult:
        return self.racer_call('tbox-retrieve', key_args)

    def tbox_retrieve1_m(self, *key_args) -> str:
        return str(self.racer_call('tbox-retrieve1', key_args))

    def tbox_retrieve1_m_(self, *key_args) -> RacerResult:
        return self.racer_call('tbox-retrieve1', key_args)

    def timenet_retrieve_m(self, *key_args) -> str:
        return str(self.racer_call('timenet-retrieve', key_args))

    def timenet_retrieve_m_(self, *key_args) -> RacerResult:
        return self.racer_call('timenet-retrieve', key_args)

    def transitive_m(self, rolename=None, tbox=None) -> str:
        return str(self.racer_call('transitive', rolename, tbox))

    def transitive_m_(self, rolename=None, tbox=None) -> RacerResult:
        return self.racer_call('transitive', rolename, tbox)

    def transitive_m_p(self, role_term=None, tbox_name=None) -> bool:
        return self.return_boolean(self.racer_call('transitive?', role_term, tbox_name))

    def unbind_m(self, name=None) -> str:
        return str(self.racer_call('unbind', name))

    def unbind_m_(self, name=None) -> RacerResult:
        return self.racer_call('unbind', name)

    def undefine_m(self, name=None) -> str:
        return str(self.racer_call('undefine', name))

    def undefine_m_(self, name=None) -> RacerResult:
        return self.racer_call('undefine', name)

    def undefquery_m(self, *key_args) -> str:
        return str(self.racer_call('undefquery', key_args))

    def undefquery_m_(self, *key_args) -> RacerResult:
        return self.racer_call('undefquery', key_args)

    def unpublish_m(self, individual=None, abox=None) -> str:
        return str(self.racer_call('unpublish', individual, abox))

    def unpublish_m_(self, individual=None, abox=None) -> RacerResult:
        return self.racer_call('unpublish', individual, abox)

    def unrelated_m(self, left_name=None, right_name=None, role_name=None) -> str:
        return str(self.racer_call('unrelated', left_name, right_name, role_name))

    def unrelated_m_(self, left_name=None, right_name=None, role_name=None) -> RacerResult:
        return self.racer_call('unrelated', left_name, right_name, role_name)

    def unsubscribe_m(self, subscriber=None, query_concept=None, abox=None) -> str:
        return str(self.racer_call('unsubscribe', subscriber, query_concept, abox))

    def unsubscribe_m_(self, subscriber=None, query_concept=None, abox=None) -> RacerResult:
        return self.racer_call('unsubscribe', subscriber, query_concept, abox)

    def with_bindings(self):
        self.push_with('with-bindings')

    def end_with_bindings(self):
        self.pop_with('with-bindings')

    def with_bindings_evaluated(self):
        self.push_with('with-bindings-evaluated')

    def end_with_bindings_evaluated(self):
        self.pop_with('with-bindings-evaluated')

    def with_critical_section(self, *key_args):
        self.push_with('with-critical-section', key_args)

    def end_with_critical_section(self):
        self.pop_with('with-critical-section')

    def with_future_bindings(self):
        self.push_with('with-future-bindings')

    def end_with_future_bindings(self):
        self.pop_with('with-future-bindings')

    def with_future_bindings_evaluated(self):
        self.push_with('with-future-bindings-evaluated')

    def end_with_future_bindings_evaluated(self):
        self.pop_with('with-future-bindings-evaluated')

    def with_nrql_settings(self, *key_args):
        self.push_with('with-nrql-settings', key_args)

    def end_with_nrql_settings(self):
        self.pop_with('with-nrql-settings')

    def with_nrql_settings_evaluated(self, *key_args):
        self.push_with('with-nrql-settings-evaluated', key_args)

    def end_with_nrql_settings_evaluated(self):
        self.pop_with('with-nrql-settings-evaluated')

    def with_unique_name_assumption(self, *key_args):
        self.push_with('with-unique-name-assumption', key_args)

    def end_with_unique_name_assumption(self):
        self.pop_with('with-unique-name-assumption')

    def without_unique_name_assumption(self, *key_args):
        self.push_with('without-unique-name-assumption', key_args)

    def end_without_unique_name_assumption(self):
        self.pop_with('without-unique-name-assumption')

    def xml_output_m(self, expr=None) -> str:
        return str(self.racer_call('xml-output', expr))

    def xml_output_m_(self, expr=None) -> RacerResult:
        return self.racer_call('xml-output', expr)

    def xml_native_output_m(self, expr=None) -> str:
        return str(self.racer_call('xml-native-output', expr))

    def xml_native_output_m_(self, expr=None) -> RacerResult:
        return self.racer_call('xml-native-output', expr)

    def xml_input_m(self, expr=None) -> str:
        return str(self.racer_call('xml-input', expr))

    def xml_input_m_(self, expr=None) -> RacerResult:
        return self.racer_call('xml-input', expr)

    def owlapi_get_last_output_stream_string_m(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_last_output_stream_string|', reasoner))

    def owlapi_get_last_output_stream_string_m_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_last_output_stream_string|', reasoner)

    def owlapi_get_last_answer_m(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_last_answer|', reasoner))

    def owlapi_get_last_answer_m_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_last_answer|', reasoner)

    def owlapi_get_i_ds_of_last_answer_m(self, reasoner=None) -> str:
        return str(self.racer_call('|_o_w_l_a_p_i-get_i_ds_of_last_answer|', reasoner))

    def owlapi_get_i_ds_of_last_answer_m_(self, reasoner=None) -> RacerResult:
        return self.racer_call('|_o_w_l_a_p_i-get_i_ds_of_last_answer|', reasoner)

    def get_namespace_prefixes_m(self) -> str:
        return str(self.racer_call('get-namespace-prefixes'))

    def get_namespace_prefixes_m_(self) -> RacerResult:
        return self.racer_call('get-namespace-prefixes')

    def ensure_small_tboxes_m(self) -> str:
        return str(self.racer_call('ensure-small-tboxes'))

    def ensure_small_tboxes_m_(self) -> RacerResult:
        return self.racer_call('ensure-small-tboxes')

    def evaluate_m(self, expr=None) -> str:
        return str(self.racer_call('evaluate', expr))

    def evaluate_m_(self, expr=None) -> RacerResult:
        return self.racer_call('evaluate', expr)

    def evaluate1_m(self, expr=None) -> str:
        return str(self.racer_call('evaluate1', expr))

    def evaluate1_m_(self, expr=None) -> RacerResult:
        return self.racer_call('evaluate1', expr)

    def exit_server(self) -> bool:
        try:
            str(self.racer_call('exit-server '))
        except BaseException:
            return True
        return False

